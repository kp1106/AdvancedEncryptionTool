import customtkinter

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    salt = b'\x8d\xb1\x9cJ}\x9b\x91\x12\x97\xb1\xd0v\xfc\xe9\xf1\xf5s\x16\xa0]=\x01a\xa4\xa9B\x8f\xa2\xc7\xc5?"'
    password = "mypassword"

    key = PBKDF2(password, salt, dkLen=32)

    entry_var = customtkinter.StringVar()
    entry = customtkinter.entry1(textvariable=entry_var)

    message = entry

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

    with open('key.bin', 'wb') as f:
        f.write(key)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame, text="/Encrypted text/")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="To encrypt...",)
entry1.pack(pady=12, padx=10)

#entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="To enter external key...", show="*")
#entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Encrypt", command=login)
button.pack(pady=12, padx=10)

#checkbox = customtkinter.CTkCheckBox(master=frame, text="Example")
#checkbox.pack(pady = 12, padx=10)

root.mainloop()