from app.models.Order import Order, OrderStatus, OrderType, OrderAction

class OrderProcessor:
    def __init__(self, account, portfolio):
        self.account = account
        self.portfolio = portfolio

    def process_order(self, order:Order):
        self.account.order_history[order.order_id] = order
        self.portfolio.pending_orders[order.order_id] = order
        if order.order_type== OrderType.MARKET:
            self.process_market_order(order)
        if order.order_type==OrderType.LIMIT:
            self.process_limit_order(order)
        return
    
    def process_market_order(self, order:Order):
        if order.action== OrderAction.BUY:
            result = self.portfolio.buy_stock(order.stock, order.quantity)
        elif order.action== OrderAction.SELL:
            result = self.portfolio.sell_stock(order.stock, order.quantity)
        if result:
            order.set_status(OrderStatus.FILLED)
            del self.portfolio.pending_orders[order.order_id]
        else:
            print("market order could not be completed")
        return False
    
    def process_stop_order(self, order:Order):
        return
    
    def process_limit_order(self, order:Order):
        return
    
    def process_stop_loss(self, order:Order):
        return
    