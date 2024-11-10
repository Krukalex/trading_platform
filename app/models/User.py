import uuid

class User:
    def __init__(self, username: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.account_id = None

    def link_account(self, account):
        from app.models.Account import Account
        """Link an Account object to this User."""
        if isinstance(account, Account):
            self.account_id = account.account_id

    def setUsername(self, name: str):
        self.username = name

    def getUsername(self):
        return self.username

    def setEmail(self, email: str):
        self.email = email
                 
    def getEmail(self):
        return self.email