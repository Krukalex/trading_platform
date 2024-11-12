import uuid
import datetime
from app.models import Stock

class Order:
    def __init__(self, order_type:str, stock:Stock, quantity:int):
        self.order_id = uuid.uuid4()
        self.order_type = order_type
        self.stock = stock
        self.quantity = quantity
        self.status = "open"
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return (f"Order({self.order_type}, Stock: {self.stock.ticker}, "
                f"Quantity: {self.quantity}, Price: {self.price}, Status: {self.status})")