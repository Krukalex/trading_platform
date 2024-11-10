import uuid

class Account:
    def __init__(self, user_id:int):
        self.account_id = uuid.uuid1()
        self.user_id = user_id
        self.balance = 0