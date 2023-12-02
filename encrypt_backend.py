from __future__ import annotations
from cryptography.fernet import Fernet

# Install using:
# pip install cryptography 

class PasswordManager:
    """Class to represent a password manager."""

    encrypted_password: bytes 
    encryption_key: bytes

    def __init__(self, inp_pwd: str):
        """Constructor for password manager."""
        # Generate random encryption key.
        self.encryption_key = Fernet.generate_key()
        # Directly encrypt password.
        self.encrypted_password = self.encrypt_password(inp_pwd)
    
    def encrypt_password(self, pwd: str) -> bytes:
        """Encrypt password and store it into a dictionary."""
        cipher = Fernet(self.encryption_key)
        # Use key to encrypt byte password.
        return cipher.encrypt(pwd.encode())
    
    def decrypt_password(self) -> str:
        """Take encrypted password and return decrypted password."""
        cipher = Fernet(self.encryption_key)
        # Decrypt using the key.
        decrypted_password = cipher.decrypt(self.encrypted_password)
        # Decode the bytes.
        return decrypted_password.decode()


def test():

    #Entry point:
    password: str = input("What password do you want encrypted? ")
    
    # Saved password as input password.
    pm: PasswordManager = PasswordManager(password)
    
    print(f"Original password: {password}")

    print (f"Encrypted Key: {pm.encryption_key}")

    print (f"Encrypted Password: {pm.encrypted_password}")

    # Decryption.
    decrypted_password: str = pm.decrypt_password()

    print (f"Decrypted Password: {decrypted_password}")
   
if __name__ == "__main__":
    test()
 