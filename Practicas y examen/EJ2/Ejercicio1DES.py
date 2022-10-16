from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class DES_CIPHER:

    BLOCK_SIZE_DES = 8 # DES: Bloque de 64 bits

    def __init__(self, key):
        """Inicializa las variables locales"""
        self.key=key

    def cifrar(self, cadena, IV):
        # Creamos un mecanismo de cifrado DES en modo CBC con una inicializacion IV
        data = cadena.encode("utf-8") # Datos a cifrar
        cipher = DES.new(self.key, DES.MODE_CBC, IV)

        # Ciframos, haciendo que data sea multiplo del tamaño de bloque
        ciphertext = cipher.encrypt(pad(data,self.BLOCK_SIZE_DES))
        # print(ciphertext)
        return ciphertext

    def descifrar(self, cifrado, IV):
        # Creamos un mecanismo de (des)cifrado DES en modo CBC con una inicializacion IV
        decipher_des = DES.new(self.key, DES.MODE_CBC, IV)

        # Desciframos, eliminamos el padding, y recuperamos la cadena
        descif = unpad(decipher_des.decrypt(cifrado), self.BLOCK_SIZE_DES).decode("utf-8", "ignore")
        print("Descifrando la anterior cadena")

        return descif

key = get_random_bytes(8) # Clave aleatoria de 64 bits 
IV = get_random_bytes(8)  # IV aleatorio de 64 bits 
datos = "Hola Mundo con DES en modo CBC"
print(datos)
d = DES_CIPHER(key)
cifrado = d.cifrar(datos, IV)
print(cifrado)
descifrado = d.descifrar(cifrado, IV)
print(descifrado)