from Crypto.Hash import HMAC, SHA512

###########################
# Ejercicio 1 - Apartado B
###########################
# Leemos el fichero de texto del ejercicio anterior

fich = open('mitexto.txt', 'r')
texto = fich.read()
fich.close()
print("-----------------------------")
print("El contenido del fichero es: ")
print(texto)
print("-----------------------------")

# Guardamos la clave secreta
secret = b'S3cr3tK3y'
print("La clave secreta es: ")
print(secret)
print("-----------------------------")

#########################
# Creamos el objeto HASH y lo generamos
#########################

h = HMAC.new(secret, digestmod=SHA512)
h.update(texto.encode('utf-8'))
print("Resultado HASH: ")
resultado = h.hexdigest()
print(resultado)

#########################
# Comprobamos la validez de HMAC-SHA512
#########################
try:
        h.hexverify(resultado)
        print("El mensaje es autentico.")
except ValueError:
        print("El mensaje o la clave es invalida")