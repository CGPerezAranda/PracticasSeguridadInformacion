from socket_class import SOCKET_SIMPLE_TCP
from rsa_class import RSA_OBJECT
from aes_class import AES_CIPHER
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64
import json

# Campos Basicos
################
OI_Str = "Comida para gatos, 1 lata"
PI_Str = "Tarjeta de credito 123456789"
RSA_Usuario = RSA_OBJECT()
RSA_Usuario.create_KeyPair()

###################################################
# A REALIZAR POR EL ALUMNO
#
# Crear una firma dual: Sig(H(H(OI) || H(PI)))
# Las variables resultantes deben ser:
# - OIMD: Hash del OI
# - PIMD: Hash del PI
# - firma_dual: Resultado de la firma dual
###################################################

# Hash OIMD
H_OIMD = SHA256.new()
H_OIMD.update(OI_Str.encode("utf-8"))
OIMD = H_OIMD.digest()

# Hash PIMD
H_PIMD = SHA256.new()
H_PIMD.update(PI_Str.encode("utf-8"))
PIMD = H_PIMD.digest()

# Concatenar OIMD y PIMD
H = OIMD+PIMD

# Hash a la concatenación
H_ALL = SHA256.new()
H_ALL.update(H)

# Guardamos el resultado del hash en fd
fd = H_ALL.digest()

# Firmamos fd para finalmente obtener la firma dual

firma_dual = RSA_Usuario.sign(fd)

###################################################
# Preparar los campos para enviarselos al vendedor
###################################################

# Mensaje para el banco (PI, firma dual, OIMD)
msg_banco = []
msg_banco.append(PI_Str)
msg_banco.append(firma_dual.hex())
msg_banco.append(OIMD.hex())
json_banco = json.dumps(msg_banco)

# Cifra el mensaje para el banco usando la clase AES
key_banco = get_random_bytes(16) # Clave aleatoria de 128 bits
IV_banco = get_random_bytes(16)  # IV aleatorio de 128 bits
AES_Usuario = AES_CIPHER(key_banco)
json_banco_cifrado = AES_Usuario.encrypt(json_banco, IV_banco)

# Cifra la clave usando la clave publica del banco (obtenida de fichero)
RSA_Banco = RSA_OBJECT()
RSA_Banco.load_PublicKey("rsa_key.pub")
digital_envelope = RSA_Banco.encrypt(key_banco)


# Enviar informacion al vendedor
################################

# Los campos son los siguientes:
# - Mensaje cifrado para el banco
# - IV usado en el mensaje cifrado para el banco
# - "digital envelope" (clave del mensaje cifrado para el banco, cifrado con kPubBanco)
# - PIMD
# - OI
# - Firma dual
# - Certificado del usuario

msg_vendedor = []
msg_vendedor.append(json_banco_cifrado.hex())
msg_vendedor.append(IV_banco.hex())
msg_vendedor.append(digital_envelope.hex())
msg_vendedor.append(PIMD.hex())
msg_vendedor.append(OI_Str)
msg_vendedor.append(firma_dual.hex())
msg_vendedor.append(RSA_Usuario.get_PublicKeyPEM().hex())
json_vendedor = json.dumps(msg_vendedor)

# Abre una conexion al vendedor
socketVendedor = SOCKET_SIMPLE_TCP('127.0.0.1', 5555)
socketVendedor.conectar()

# Envia los datos
print("Cliente -> Vendedor: mensaje")
socketVendedor.enviar(json_vendedor.encode("utf-8"))

# Cierra el canal
socketVendedor.cerrar()

print("Cliente finalizado correctamente")