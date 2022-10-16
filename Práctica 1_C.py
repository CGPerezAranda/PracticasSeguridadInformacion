def cifradoCesarAlfabetoIngles(cadena, clave):
    """Devuelve un cifrado Cesar tradicional (+i)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 65) + clave) % 26) + 65
        # Tratamiento de las minúsculas
        if (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + clave) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

def desCifradoCesarAlfabetoIngles(cadena, clave):
    """Descifra Cesar tradicional"""
    resultado = ''
    i = 0
    while i < len(cadena):
        ordenCifrado = ord (cadena[i])
        ordenClaro = 0
        if(ordenCifrado >= 65 and ordenCifrado <= 90):
           ordenClaro = (((ordenCifrado - 65) - clave) % 26) + 65 
        # Tratamiento de las minúsculas
        if(ordenCifrado >= 97 and ordenCifrado <= 122):
           ordenClaro = (((ordenCifrado - 97) - clave) % 26) + 97 
        resultado = resultado + chr(ordenClaro)
        i = i + 1
    return resultado



print("Introduzca un texto para realizar el cifrado Cesar:")
texto = input()
print("Introduzca una clave para realizar el cifrado:")
clave = int(input()) % 27

print(texto)
print("Clave elegida:")
print(clave)
print("Texto Cifrado")
cifradoCESAR = cifradoCesarAlfabetoIngles(texto,clave) 
print(cifradoCESAR)
print("Texto Descifrado")
descifradoCESAR = desCifradoCesarAlfabetoIngles(cifradoCESAR,clave) 
print(descifradoCESAR)
