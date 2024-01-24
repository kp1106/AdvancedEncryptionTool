from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

salt = b'\x8d\xb1\x9cJ}\x9b\x91\x12\x97\xb1\xd0v\xfc\xe9\xf1\xf5s\x16\xa0]=\x01a\xa4\xa9B\x8f\xa2\xc7\xc5?"'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

userInput = input("Enter a string to encrypt: ")
byte_object_2=bytes(userInput,"utf-8")

message = byte_object_2

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)


with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()


cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

print("DATA HAS BEEN ENCRYPTED VIA AES INTO 8 BIT BINARY BELOW:")
print(cipher)
print("DATA HAS BEEN DECRYPTED VIA KEY STORED LOCALLY BELOW:")
print(original)

with open('key.bin', 'wb') as f:
    f.write(key)