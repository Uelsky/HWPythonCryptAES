import hashlib

from Crypto.Cipher import AES
from encoding import encoding


cipher_text = encoding("top secret")
BS = AES.block_size
iv = cipher_text[:BS]
unpad = lambda s: s[:-ord(s[len(s)-1:])]

for k in range(100, 1000):
    key = hashlib.sha256(str(k).encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text[BS:]))

    # Расшифровка произойдет на ключе 476
    print(f"Attempt with key {k}:", str(plain_text))