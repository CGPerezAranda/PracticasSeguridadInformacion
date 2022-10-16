def descifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve la cadena descifrada en Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        cadenaCifrada = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (cadenaCifrada >= 65 and cadenaCifrada <= 90):
            ordenCifrado = (((cadenaCifrada - 65) - 3) % 26) + 65
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

cadenaCifrada = 'YHQL YLGL YLQFL CHWD'
print(cadenaCifrada)
cifradoCESAR = descifradoCesarAlfabetoInglesMAY(cadenaCifrada) 
print(cifradoCESAR)