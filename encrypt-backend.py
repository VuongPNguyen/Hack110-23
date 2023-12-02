from cryptography.fernet import Fernet

class PasswordManager:
    """Class to represent a password manager."""

    password: str 
    encrypted_key: bytes
    password_key_dict: dict[str, bytes]

    def __init__(self, inp_pwd: str):
        """Constructor for password manager."""
        self.password = inp_pwd
        self.encryption_key = Fernet.generate_key()
        self.password_key_dict = {}
    
    def encrypt_password(self):
        """Encrypt password and store it into a dictionary."""
        cipher = Fernet(self.encryption_key)
        encrypted_password = cipher.encrypt(self.password.encode())
        self.password_key_dict[self.password] = encrypted_password
    
    def decrypt_password(self, encrypted_password: bytes) -> str:
        """Take encrypted password and return decrypted password."""
        cipher = Fernet(self.encryption_key)
        decrypted_password = cipher.decrypt(encrypted_password)
        return decrypted_password.decode()


def main():

    #Entry point:
    password: str = input("What password do you want encrypted? ")
    
    # Saved password as input password.
    pm: PasswordManager = PasswordManager(password)
    
    # Password has been encrytped and added to a dictonary
    pm.encrypt_password()
    
    # Retrieve the encrytped password and encryption key.
    encrypted_password: bytes = pm.password_key_dict[password]
    encryption_key: bytes = pm.encryption_key

    print(f"Original password: {password}")

    print (f"Encrypted Password: {encryption_key}")

    # Decryption.
    manager_decryption: PasswordManager = PasswordManager(password)
    manager_decryption.encryption_key = encryption_key
    decrypted_password: str = manager_decryption.decrypt_password(encrypted_password)

    print (f"Decrypted Password: {decrypted_password}")
   
if __name__ == "__main__":
    main()
 