def cifradoCesarAlfabetoInglesMAY(cadena, j):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # MAYUSCULAS - Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + j) % 26) + 65
        # MINUSCULAS - Cambia el caracter a cifrar
        if (ordenClaro >= ord("a") and ordenClaro <= ord("z")):
            ordenCifrado = (((ordenClaro - 97) + j) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

claroCESAR = 'VENI VIDI VINCI ZETA'
print("Texto a cifrar: " + claroCESAR)
cifradoCESAR = cifradoCesarAlfabetoInglesMAY(claroCESAR, 3) 
print("Texto cifrado: " + cifradoCESAR)

def descifradoCesarAlfabetoInglesMAY(cadena, j):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # MAYUSCULAS - Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) - j) % 26) + 65
        # MINUSCULAS - Cambia el caracter a cifrar
        if (ordenClaro >= ord("a") and ordenClaro <= ord("z")):
            ordenCifrado = (((ordenClaro - 97) - j) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

print()
claroCESAR = 'YHQL YLGL YLQFL CHWD'
print("Texto para cifrar: " + claroCESAR)
cifradoCESAR = descifradoCesarAlfabetoInglesMAY(claroCESAR, 3) 
print("Texto cifrado: " + cifradoCESAR)