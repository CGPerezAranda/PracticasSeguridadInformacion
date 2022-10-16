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

# Crea el socket servidor y escucha
print("Creando socket y escuchando...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5557)
socket.escuchar()

#Virs yra gerai, apacioj nezinau
t_alice, t_bob, t_random = msg_a_t
t_random = bytearray.fromhex(t_random)
key_a_b = get_random_bytes(16)

datos = socket.recibir()
decipher_aes_a_b1 = AES.new(key_a_b1, AES.MODE_ECB)
json_b1_a = unpad(decipher_aes_a_b1.decrypt(datos), BLOCK_SIZE_AES).decode("utf-8")
print("T->A (Clear): " + json_b1_a)
msg_b1_a = json.loads(json_b1_a)