#!/usr/local/bin/python3
from cryptography.fernet import Fernet
def key_generator():
    key=Fernet.generate_key()
    cipher=Fernet(key)
    with open('Secret.Key', 'wb') as file:
        file.write(key)
    return cipher
