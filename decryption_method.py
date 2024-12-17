#!/usr/local/bin/python3
import os
from cryptography.fernet import Fernet

target_file_path='first'
target_file='fourth'
key_file='Secret.Key'

def decryption(target_file_path, target_file, key_file):
    #Read the encryption key
    with open(key_file, 'rb') as f:
        k=f.read()
    fernet=Fernet(k)

    #Traverse the directory to find the target file
    for dirpath, dirnames, filenames in os.walk(target_file_path):
        for filename in filenames:
            if filename == target_file:
                file_path=os.path.join(dirpath, filename)

                #Read the encrypted data
                with open(file_path, 'rb') as f:
                    file_data=f.read()

                #Decrypt the data
                decrypted_data=fernet.decrypt(file_data)
                    decrypted_data=fernet.decrypt(file_data)

                #Write the decrypted data back to the same file
                with open(file_path, 'wb') as f:
                    f.write(decrypted_data)

                print(f"Decrypted: {file_path}")


#Call the function
decryption(target_file_path, target_file, key_file)
