import uuid

class Account:
    def __init__(self, user):
        from app.models.User import User 
        self.account_id = str(uuid.uuid4())
        self.user_id = user.user_id
        self.balance = 0
        user.link_account(self)