from app.models import Stock
import uuid
import datetime

class Trade:
    def __init__(self, trade_type:str, stock:Stock, quantity:float, trade_fee:float, new_balance:float):
        self.trade_id = uuid.uuid4()
        self.trade_type = trade_type
        self.stock = stock
        self.quantity = quantity
        self.trade_fee = trade_fee
        self.cost = round(stock.get_price()*quantity,2)+self.trade_fee
        self.new_balance = new_balance
        self.timestamp = datetime.datetime.now()
    
    def __repr__(self) -> str:
        return f"Trade({self.trade_type}, {self.stock}, Quantity: {self.quantity}, Trade Fees: {self.trade_fee}, Total Cost: {self.cost}, New Balance: {self.new_balance})"