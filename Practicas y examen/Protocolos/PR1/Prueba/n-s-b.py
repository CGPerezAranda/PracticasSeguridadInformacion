from Crypto.Cipher import PKCS1_OAEP, DES, AES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, HMAC
from Crypto.Signature import pss
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import base64
import json
from socket_class import SOCKET_SIMPLE_TCP

# Parametros
key_b_t = b'FEDCBA9876543210'
BLOCK_SIZE_AES = 16

# Abre una conexion a Alice
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 7777)
socket.escuchar()

# A->B: Alice, Bob
datos = socket.recibir()
json_a_b = datos.decode("utf-8" ,"ignore")
print("A->B: " + json_a_b)
msg_a_b = json.loads(json_a_b)