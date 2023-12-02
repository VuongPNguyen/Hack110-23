from encrypt_backend import PasswordManager

class acct_pwd:

    # Used for display and sort
    account: str
    lower_account: str

    # Automatically encrypted.
    passwordManager: PasswordManager
    
    def __init__(self, account: str, password: str):
        self.account = account
        self.lower_account = account.lower()
        self.passwordManager = PasswordManager(password)