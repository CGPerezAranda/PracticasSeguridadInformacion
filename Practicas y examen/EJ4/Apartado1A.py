from Crypto.Hash import SHA512

###########################
# Ejercicio 1 - Apartado A
###########################
# Creamos el fichero de texto

fichero = open('mitexto.txt', 'w')
fichero.write('Jesus')
fichero.write('\n')
fichero.write('Sanchez Fernandez')
fichero.close()

#########################
# Creamos el objeto HASH y lo generamos
#########################
# SI PREFIERES NO CODIFICAR SE ABRE COMO -rb- para lectura binaria
fich = open('mitexto.txt', 'r')

texto = fich.read()
fich.close()
print("Contenido del fichero: ")
print(texto)
print()

# SHA512 SOLO TRABAJA EN BINARIO, HAY QUE CODIFICAR
ho = SHA512.new(data=texto.encode("utf-8"))
print("Resultado HASH: ")
print(ho.hexdigest())