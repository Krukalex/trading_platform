import uuid
import datetime
from app.models import Stock
from enum import Enum

class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"

class OrderAction(Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderStatus(Enum):
    OPEN = "OPEN"
    FILLED = "FILLED"
    PARTIALLY_FILLER = "PARTIALLY FILLED"
    CANCELLED = "CANCELLED"

class Order:
    def __init__(self, order_type:OrderType, action:OrderAction, stock:Stock, quantity:int):
        self.order_id = uuid.uuid4()
        self.order_type = order_type
        self.action = action
        self.stock = stock
        self.quantity = quantity
        self.status = OrderStatus.OPEN
        self.created_at = datetime.datetime.now()

    def set_status(self, status:OrderStatus):
        self.status = status

    def __repr__(self):
        return (f"Order({self.order_type.name}, Stock: {self.stock.ticker}, "
                f"Quantity: {self.quantity}, Action: {self.action.name}, Status: {self.status.name})")
    
class MarketOrder(Order):
    def __init__(self, order_type: OrderType, action: OrderAction, stock: Stock, quantity: int):
        super().__init__(order_type, action, stock, quantity)

class LimitOrder(Order):
    def __init__(self, order_type: OrderType, action: OrderAction, limit:str, stock: Stock, quantity: int):
        super().__init__(order_type, action, stock, quantity)
        self.limit = limit
    
    def __repr__(self):
        return super().__repr__() + f", Limit: {self.limit}"
    
class StopOrder(Order):
    def __init__(self, order_type: OrderType, action: OrderAction, stop:str, stock: Stock, quantity: int):
        super().__init__(order_type, action, stock, quantity)
        self.stop = stop

    def __repr__(self):
        return super().__repr__() + f", Stop: {self.stop}"