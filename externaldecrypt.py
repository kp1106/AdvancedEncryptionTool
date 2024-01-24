from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

salt = b'\x8d\xb1\x9cJ}\x9b\x91\x12\x97\xb1\xd0v\xfc\xe9\xf1\xf5s\x16\xa0]=\x01a\xa4\xa9B\x8f\xa2\xc7\xc5?"'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

print(original)