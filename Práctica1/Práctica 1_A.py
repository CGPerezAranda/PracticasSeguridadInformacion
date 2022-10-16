def cifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + 3) % 26) + 65
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

def desCifradoCesarAlfabetoInglesMAY(cadena):
    """Descifra Cesar tradicional"""
    resultado = ''
    i = 0
    while i < len(cadena):
        caracterPorDescifrar = ord (cadena[i])
        caracterDescifrado = 0
        if(caracterPorDescifrar >= 65 and caracterPorDescifrar <= 90):
           caracterDescifrado = (((caracterPorDescifrar - 65) - 3) % 26) + 65 
        resultado = resultado + chr(caracterDescifrado)
        i = i + 1
    return resultado




claroCESAR = 'VENI VIDI VINCI ZETA'
print(claroCESAR)
cifradoCESAR = cifradoCesarAlfabetoInglesMAY(claroCESAR) 
print(cifradoCESAR)
descifradoCESAR = desCifradoCesarAlfabetoInglesMAY(cifradoCESAR)
print(descifradoCESAR)