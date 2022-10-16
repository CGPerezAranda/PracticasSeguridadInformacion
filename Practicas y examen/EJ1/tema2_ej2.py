def cifradoMono(cadena, clave):
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    # Cuenta la palabra "CIFRA"
    j = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenClave = ord(clave[j])
        
        ordenCifrado = 0
        # MAYUSCULAS - Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            suma = (ordenClave - 65) + 1
            ordenCifrado = (((ordenClaro - 65) + suma) % 26) + 65
            # print(str(ordenClaro) + " + " + str(suma) + " = " + str(ordenCifrado))

        # print("Letra: " + cadena[i] + " ordenClaro = " + str(ordenClaro))
        # print("letra: " + clave[j] + " ordenClave = " + str(ordenClave))
        # print(str((ordenClaro - 65) - (ordenClave - 65 )))
        # print("------------------")

        # MINUSCULAS - Cambia el caracter a cifrar
        if (ordenClaro >= ord("a") and ordenClaro <= ord("z")):
            ordenCifrado = (((ordenClaro - 97) + ordenClave) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
        if ( j is len(clave)-1):
            j = 0
        else:
            j = j +1
        
    # devuelve el resultado
    return resultado

textoClaro = 'HOLAAMIGOS'
clave = 'CIFRA'
print("Texto a cifrar: " + textoClaro)
textoCifrado = cifradoMono(textoClaro, clave) 
print("Texto cifrado: " + textoCifrado)