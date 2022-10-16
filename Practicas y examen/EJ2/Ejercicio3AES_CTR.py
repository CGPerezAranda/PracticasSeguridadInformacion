from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class AES_CIPHER:

    BLOCK_SIZE_AES = 16 # AES: Bloque de 128 bits

    def __init__(self, key):
        """Inicializa las variables locales"""
        self.key=key

    def cifrar(self, cadena):
        # Creamos un mecanismo de cifrado AES en modo ECB con una inicializacion IV
        data = cadena.encode("utf-8") # Datos a cifrar
        cipher = AES.new(self.key, AES.MODE_ECB)

        # Ciframos, haciendo que data sea multiplo del tamaño de bloque
        ciphertext = cipher.encrypt(pad(data,self.BLOCK_SIZE_AES))
        print(ciphertext)
        return ciphertext

    def descifrar(self, cifrado):
        # Creamos un mecanismo de (des)cifrado AES en modo ECB con una inicializacion IV
        decipher_aes = AES.new(key, AES.MODE_ECB)

        # Desciframos, eliminamos el padding, y recuperamos la cadena
        descif = unpad(decipher_aes.decrypt(cifrado), self.BLOCK_SIZE_AES).decode("utf-8", "ignore")
        print("Descifrando la anterior cadena en AES en modo ECB")
        print(descif)
        return descif

key = get_random_bytes(16) # Clave aleatoria de 128 bits 
datos = "Hola Mundo con AES en modo ECB"
print(datos)
d = AES_CIPHER(key)
cifrado = d.cifrar(datos)
descifrado = d.descifrar(cifrado)