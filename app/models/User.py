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

    def set_username(self, name: str):
        self.username = name
    def get_username(self):
        return self.username
    def set_email(self, email: str):
        self.email = email      
    def get_email(self):
        return self.email