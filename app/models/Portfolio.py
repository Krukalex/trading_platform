from app.models import Account, Stock, Order
from app.models.Trade import Trade

import uuid

class Portfolio:
    def __init__(self, account:Account):
        self.portfolio_id = uuid.uuid1()
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
    def deduct_value(self, amount:float):
        self.total_value-=amount
    
    def buy_stock(self, stock:Stock, quantity:int=1)->bool:
        total_price = round(quantity * stock.get_price(),2)
        trade_fee = round(total_price * self.account.trade_fee_rate,2)

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

        trade = Trade(
            trade_type="Stock Purchase",
            stock=stock,
            quantity=quantity,
            trade_fee=trade_fee,
            new_balance=self.account.get_balance()
        )
        self.account.trade_history.append(trade)
        print(f"Purchased {quantity} shares of {stock.ticker} for a price of {total_price} plus a trade fee of {trade_fee}. Account balance is {self.account.get_balance()}")
        return True
    
    def sell_stock(self, stock:Stock, quantity:int = 1):
        total_profit = round(quantity * stock.get_price(),2)
        trade_fee = round(total_profit * self.account.trade_fee_rate,2)

        if stock.ticker not in self.holdings:
            print(f"You do not currently own {stock.company_name} stock. This sale is invalid")
            return False
        elif quantity>self.holdings[stock.ticker]['quantity']:
            print(f"You are attempting to sells {quantity} shares of {stock.ticker}, but you only are holding {self.holdings[stock.ticker]['quantity']} shares. This sale is invalid")
            return False
        else:
            self.holdings[stock.ticker]["value"]-=(total_profit)
            self.holdings[stock.ticker]["quantity"]-=quantity

        self.deduct_value(total_profit)

        self.account.apply_trade_fee(total_profit)
        self.account.add_balance(total_profit)

        trade = Trade(
            trade_type="Stock Sale",
            stock=stock,
            quantity=quantity,
            trade_fee=trade_fee,
            new_balance=self.account.get_balance()
        )
        self.account.trade_history.append(trade)
        print(f"Sold {quantity} shares of {stock.ticker} for a profit of {total_profit} minus a trade fee of {trade_fee}. Account balance is {self.account.get_balance()}")
        return True
    
    def create_order(self, stock:Stock, quantity:int, order_type:str):
        order = Order(
            order_type=order_type,
            stock=stock,
            quantity=quantity
        )

    def get_holdings(self):
        print(self.holdings)