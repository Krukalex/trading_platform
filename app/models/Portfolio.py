from app.models import Account

class Portfolio:
    def __init__(self, account:Account):
        self.account_id = account.get_account_id()
        self.user_id = account.get_user_id()
        self.holdings = []
        self.total_value = 0

