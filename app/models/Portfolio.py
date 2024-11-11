from app.models import Account, Stock

class Portfolio:
    def __init__(self, account:Account):
        self.account_id = account.get_account_id()
        self.user_id = account.get_user_id()
        self.holdings = {}
        self.total_value = 0
        self.account = account

    
    def get_total_value(self):
        return self.total_value
    def set_total_value(self, value:float):
        self.total_value = value
    def get_account_id(self):
        return self.account_id
    def get_user_id(self):
        return self.user_id
    def add_value(self, amount:float):
        self.total_value+=amount
    
    def buy_stock(self, stock:Stock, quantity:int=1)->bool:
        total_price = quantity * stock.get_price()
        trade_fee = total_price * self.account.trade_fee_rate

        if total_price+trade_fee>self.account.get_balance():
            print(f"Insufficent funds, attempting to make purches for {total_price}. Account balance is {self.account.get_balance()}")
            return False

        if stock.ticker in self.holdings:
            self.holdings[stock.ticker]["value"]+=total_price
            self.holdings[stock.ticker]["quantity"]+=quantity
        else:
            self.holdings[stock.ticker]= {
                "value": total_price,
                "quantity": quantity
            }
        self.add_value(total_price)

        self.account.apply_trade_fee(total_price)
        self.account.deduct_balance(total_price)
        print(f"Purchased {quantity} shares of {stock.ticker} for a price of {total_price}. Account balance is {self.account.get_balance()}")
        return True

    def get_holdings(self):
        print(self.holdings)


