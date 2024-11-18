import uuid
from app.models.Stock import Stock

class User:
    def __init__(self, username: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.account_id = None
        self.watchlist = {}

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
    
    def add_to_watchlist(self, stock: Stock):
        if stock.stock_id not in self.watchlist:
            self.watchlist[stock.stock_id] = stock
        else:
            print(f"Stock {stock.ticker} is already in the watchlist.")

    def remove_from_watchlist(self, stock:Stock):
        if stock.stock_id in self.watchlist:
            del self.watchlist[stock.stock_id]
        else:
            print(f"Stock {stock.ticker} is not in the watchlist")

    def view_watchlist(self):
        if not self.watchlist:
            print("Your watchlist is empty")
            return
        for stock_id, stock in self.watchlist.items():
            print(f"{stock.ticker_symbol} - {stock.company_name} - Current Price: {stock.get_price()}")