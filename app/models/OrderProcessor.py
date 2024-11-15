from app.models.Order import Order, OrderStatus, OrderType, OrderAction
import threading

class OrderProcessor:
    def __init__(self, account, portfolio):
        self.account = account
        self.portfolio = portfolio
        self.lock = self.portfolio.lock
        self.running = True
    
    def process_market_order(self, order:Order):
        if order.action== OrderAction.BUY:
            result = self.portfolio.buy_stock(order.stock, order.quantity)
        elif order.action== OrderAction.SELL:
            result = self.portfolio.sell_stock(order.stock, order.quantity)
        if result:
            order.set_status(OrderStatus.FILLED)
            with self.lock:
                del self.portfolio.pending_orders[order.order_id]
            return True
        else:
            print("market order could not be completed")
        return False
    
    def process_stop_order(self, order:Order):
        if order.action == OrderAction.BUY:
            print(order.stock.get_price())
            print(order.stop)
            if order.stock.get_price()>order.stop:
                result = self.portfolio.buy_stock(order.stock, order.quantity)
            else:
                #need to add order to a queue that polls the stock price on a scheduled basis
                result = None
                print("Sell stop order not executed since stock was not above the required price")
        elif order.action == OrderAction.SELL:
            if order.stock.get_price()<order.stop:
                result = self.portfolio.sell_stock(order.stock, order.quantity)
            else:
                result = None
                print("Sell stop order not executed since stock did not drop below the required price")
        if result:
            order.set_status(OrderStatus.FILLED)
            with self.lock:
                del self.portfolio.pending_orders[order.order_id]
            return True
        return False
    
    def process_limit_order(self, order:Order):
        return
    
    def process_stop_loss(self, order:Order):
        return
    
    def procces_order_queue(self):
        def process_queue():
            with self.lock:
                for identifier, order in self.portfolio.pending_orders.items():
                    print(order.order_type)
                    print(order.stock.price)
                    print(order.stop)
                    if order.order_type == OrderType.STOP:
                        if order.stock.price > order.stop:
                            self.process_stop_order(order)
                    if order.order_type == OrderType.LIMIT:
                        if order.stock.price < order.limit:
                            self.process_limit_order(order)
        
        def run_processor(interval = 10):
            if self.running:
                process_queue()
                timer = threading.Timer(interval, run_processor)
                timer.daemon = True
                timer.start()
        
        run_processor()
        return

    def stop_order_processing_queue(self):
        self.running = False