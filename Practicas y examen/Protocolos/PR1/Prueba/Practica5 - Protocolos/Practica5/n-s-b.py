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

# B: Crear campos
b_alice = "Alice"
b_bob = "Bob"
b_random = get_random_bytes(8)

# Crea el socket y escucha
print("Creando socket y escuchando...")
socket = SOCKET_SIMPLE_TCP('127.0.0.2', 7777)
socket.escuchar()

# A->B: Ra
datos = socket.recibir()
json_a_b = datos.decode("utf-8" ,"ignore")
msg_a_b = json.loads(json_a_b)
msg_t_b_enc = msg_a_b[0]
msg_t_b_enc = bytearray.fromhex(msg_t_b_enc)
decipher_aes_b_t = AES.new(key_b_t, AES.MODE_ECB)
json_t_b = unpad(decipher_aes_b_t.decrypt(msg_t_b_enc), BLOCK_SIZE_AES).decode("utf-8")
print("T->B (Des): " + json_t_b)
msg_t_b = json.loads(json_t_b)

# B: Guardar random K_AB y crea random K_B
t_k_ab, t_alice = msg_t_b
t_k_ab = bytearray.fromhex(t_k_ab)
b_random = get_random_bytes(8)

# B: Comprobar msg_t_b
if (b_alice != t_alice):
    print("ERROR: Emisor incorrecto.")
    socket.cerrar()
    exit()

# B: msg_b_a = E_AB(Rb)
msg_b_a = []
msg_b_a.append(b_random.hex())

# B->A: E_AB(msg_t_a)
json_b_a = json.dumps(msg_b_a)
cipher_aes_b_a = AES.new(t_k_ab, AES.MODE_ECB)
datos = cipher_aes_b_a.encrypt(pad(json_b_a.encode("utf-8"),BLOCK_SIZE_AES))

print("B->A (Des): " + json_b_a)
socket.enviar(datos)

# A->B: E_AB(Rb-1)
# B: Descifrar msg_a_b
datos = socket.recibir()
decipher_aes_a_b = AES.new(t_k_ab, AES.MODE_ECB)
json_a_b = unpad(decipher_aes_a_b.decrypt(datos), BLOCK_SIZE_AES).decode("utf-8")
print("A->B (Des): " + json_a_b)
msg_a_b = json.loads(json_a_b)

# B: Comprobar msg_a_b

b_random_a_1 = msg_a_b[0]
b_random_a_1 = bytearray.fromhex(b_random_a_1)
b_random_b_1 = int.from_bytes(b_random,byteorder='big') - 1
b_random_b_1 = b_random_b_1.to_bytes(len(b_random),byteorder='big')
if (b_random_a_1 != b_random_b_1):
    print("ERROR: Rb incorrecta")
    socket.cerrar()
    exit()

# Hemos terminado la conexion con T
# Cerramos el socket
socket.cerrar()