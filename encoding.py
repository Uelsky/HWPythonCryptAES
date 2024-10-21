import hashlib

from Crypto.Cipher import AES
from Crypto import Random


def encoding(plain_text):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    key = hashlib.sha256(b"476").digest()

    plain_text = pad(plain_text)
    iv = Random.new().read(BS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = (iv + cipher.encrypt(plain_text.encode()))

    return cipher_text
