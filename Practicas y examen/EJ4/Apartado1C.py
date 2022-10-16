from Crypto.Hash import SHA3_256

###########################
# Ejercicio 1 - Apartado C
###########################
# Creamos el objeto hash
h = SHA3_256.new()
#Abrimos el fichero y leemos de 4 en 4 bytes
file = open("EJ4/test.docx", "rb")
# Leer la primera linea
bin = file.read(4 * 1024)
while (bin != b''):
     # Actualizamos el hash por cada linea
     h.update(bin)
     # Volver a leer otra linea
     bin = file.read(4 * 1024)
file.close()

# Visualizamos el hash
print()
print("HASH: ")
print(h.hexdigest())