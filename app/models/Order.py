import uuid
import datetime
from app.models import Stock

class Order:
    def __init__(self, order_type:str, action:str, stock:Stock, quantity:int):
        self.order_id = uuid.uuid4()
        self.order_type = order_type
        self.action = action
        self.stock = stock
        self.quantity = quantity
        self.status = "open"
        self.created_at = datetime.datetime.now()

    def set_status(self, status:str):
        self.status = status

    def __repr__(self):
        return (f"Order({self.order_type}, Stock: {self.stock.ticker}, "
                f"Quantity: {self.quantity}, Status: {self.status})")