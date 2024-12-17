# File Encryption & Decryption Tool

This is a Python-based tool designed to automatically encrypt and decrypt files in directories and subdirectories. The tool is built with simplicity and security in mind, ensuring that users can protect their sensitive data effortlessly.

## Features

- Encrypt and decrypt files in specified directories and subdirectories.
- Strong encryption using symmetric AES encryption algorithm.
- Simple command-line interface (CLI) for ease of use.
- Automatically processes all files in a given directory.
  
## Prerequisites

- Python 3.x
- `pycryptodome` library for encryption (can be installed via pip)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dark5301/Encryption_Decryption.git

# Navigate to project folder 

cd Encryption_Decryption

# Install the required dependencies

pip install -r requirements.txt

# How It Works

Encryption: The tool uses the AES (Advanced Encryption Standard) symmetric encryption algorithm to encrypt files. A password provided by the user is used to generate an encryption key, which is then applied to all files in the specified directory.
Decryption: Decryption works by applying the same AES algorithm with the correct password to reverse the encryption process and restore the original files.
Security Considerations

Ensure the password used for encryption is strong and kept secure.
The password should be the same for both encryption and decryption.
Encrypted files can only be decrypted with the correct password. There is no way to recover the original files without it.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgements

This tool uses the pycryptodome library for encryption.
Thanks to the open-source community for their contributions and support.


