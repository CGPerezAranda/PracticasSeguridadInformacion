from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class DES_CIPHER:

    BLOCK_SIZE_DES = 8 # DES: Bloque de 64 bits

    def __init__(self, key):
        """Inicializa las variables locales"""

        cipher = DES.new(key, DES.MODE_CBC, IV)

    def cifrar(self, cadena, IV):
        """Cifra el parámetro cadena (de tipo String) con una IV específica, y devuelve el texto cifrado binario"""

        # Ciframos, haciendo que data sea multiplo del tamaño de bloque
        ciphertext = self.cipher.encrypt(pad(data,BLOCK_SIZE_DES))

        # Mostramos el cifrado por pantalla en modo binario y en modo base 64
        print(ciphertext)
        encoded_ciphertext = base64.b64encode(ciphertext)
        print(encoded_ciphertext)

    def descifrar(self, cifrado, IV):
        """Descrifra el parámetro cifrado (de tipo binario) con una IV específica, y devuelve la cadena en claro de tipo String"""


key = get_random_bytes(8) # Clave aleatoria de 64 bits
IV = get_random_bytes(8) # IV aleatorio de 64 bits
datos = "Hola Mundo con DES en modo CBC".encode("utf-8")
print(datos)
d = DES_CIPHER(key)
cifrado = d.cifrar(datos, IV)
descifrado = d.descifrar(cifrado, IV)