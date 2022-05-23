#!/usr/bin/env python3

import os
from cryptography.fernet import Frenet

#lets find some files

files = []

for file in os.listdir():
        if file == "voldimrt.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)


with open("thekey.key", "rb") as key:
        secretkey = key.read()
        
passphrase = "coffee"

user_phrase = input("enter the passphrase to decrypt files\n")

if user_phrase == passphrase:
	print("decryption innitiated")
	for file in files:
        	with open(file, "rb") as thefile:
                	contents = thefile.read()
	        contents_decrypted = Fernet(secretkey).decrypt(contents)
        	with open(file, "wb") as thefile:
                	thefile.write(contents_decrypted)
else:
	print("wrong passphrase")
