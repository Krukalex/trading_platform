from app.models import User, Account, Portfolio, Stock
from app.models.Order import OrderAction, OrderType
from app.models.OrderProcessor import OrderProcessor
import time
import signal
import logging

alex = User("Alex", "Alex@example.com")
alex_account = Account(alex)
alex_account.deposit(1000)

mike = User("Mike", "Mike@example.com")
mike_account = Account(mike)

alex_portfolio = Portfolio(alex_account)

aapl = Stock("Apple", "AAPL", 100)
msft = Stock("Microsoft", "MSFT", 120)

processor = OrderProcessor(alex_account, alex_portfolio)
processor.procces_order_queue()

def signal_handler(sig, frame):
    # Gracefully stop the application when SIGINT (Ctrl+C) is received
    logging.info("Gracefully stopping the application...")
    processor.stop_order_processing_queue()
    exit(0)

if __name__ == "__main__":
    print(".........................Running.........................")
    signal.signal(signal.SIGINT, signal_handler)

    alex_portfolio.create_stop_order(msft, 2, OrderType.STOP, OrderAction.BUY, stop=140)

    try:
        while True:
            # This will keep the main thread alive, allowing background threads to run
            time.sleep(1)
            msft.set_price(150)
            alex_account.get_order_history()
            if not alex_portfolio.pending_orders:
                alex_portfolio.create_market_order(aapl, 3, OrderType.MARKET, OrderAction.BUY)
    except KeyboardInterrupt:
        logging.info("Application terminated")
    print(".........................End.........................")
    # app.run(debug=True)