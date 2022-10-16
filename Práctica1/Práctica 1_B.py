def cifradoCesarAlfabetoIngles(cadena):
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
        # Tratamiento de las minúsculas
        if (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + 3) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

def desCifradoCesarAlfabetoIngles(cadena):
    """Descifra Cesar tradicional"""
    resultado = ''
    i = 0
    while i < len(cadena):
        caracterPorDescifrar = ord (cadena[i])
        caracterDescifrado = 0
        if(caracterPorDescifrar >= 65 and caracterPorDescifrar <= 90):
           caracterDescifrado = (((caracterPorDescifrar - 65) - 3) % 26) + 65 
        # Tratamiento de las minúsculas
        if(caracterPorDescifrar >= 97 and caracterPorDescifrar <= 122):
           caracterDescifrado = (((caracterPorDescifrar - 97) - 3) % 26) + 97 
        resultado = resultado + chr(caracterDescifrado)
        i = i + 1
    return resultado




print ('--------------Apartado B--------------')
claroCESAR = 'VEni viDI VINCI Zeta'
print(claroCESAR)
cifradoCESAR = cifradoCesarAlfabetoIngles(claroCESAR) 
print(cifradoCESAR)
descifradoCESAR = desCifradoCesarAlfabetoIngles(cifradoCESAR)
print(descifradoCESAR)