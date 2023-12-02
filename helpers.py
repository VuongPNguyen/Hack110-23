class acct_pwd:
    account: str
    lower_account: str
    password: str
    
    def __init__(self, account: str, password: str):
        self.account = account
        self.lower_account = account.lower()
        self.password = password