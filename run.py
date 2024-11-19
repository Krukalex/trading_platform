from app.models import User, Account, Portfolio, Stock, StockManager
from app.models.Order import OrderAction, OrderType
from app.models.OrderProcessor import OrderProcessor
from app.models.StockManager import StockManager
import time
import signal
import logging

alex = User("Alex", "Alex@example.com")
stock_manager = StockManager()
alex_account = Account(alex)
alex_account.deposit(1000)
alex_portfolio = Portfolio(alex_account, stock_manager)


def process_user_input():
    action = input("What would you like to do: trade, get_balance, get_stock_price? ").upper()
    if action not in ["TRADE", "GET_BALANCE", "GET_STOCK_PRICE"]:
        print('Invalid action, please choose one of the given options')
        return
    if action == "TRADE":
        buy_sell_stock()
    elif action == "GET_BALANCE":
        print(f"Your current balance is {alex_account.get_balance()}")
        return
    elif action == "GET_STOCK_PRICE":
        ticker = input("choose a ticker to get the price for. ").upper()
        stock = stock_manager.get_stock(ticker)
        print(f"The current price of {stock.ticker} is {stock.price}")
        return
        

def buy_sell_stock():
    action = input("What action would you like to take? (BUY/SELL): ").upper()
    if action not in ["BUY", "SELL"]:
        print("Invalid action. Please choose either 'BUY' or 'SELL'.")
        return
    
    quantity = input("How many shares? ")
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid input for quantity. Please enter a valid number.")
        return

    ticker = input("Which stock would you like to choose? (e.g., AAPL, MSFT): ").upper()

    if ticker is None:
        print(f"Stock symbol {ticker} not found. Please try again.")
        return
    
    order_type = input("What type of order would you like to make? (MARKET/STOP/LIMIT): ").upper()
    if order_type not in ["MARKET", "STOP", "LIMIT"]:
        print("Invalid order type. Please choose either 'MARKET', 'STOP', or 'LIMIT'.")
        return
    
    stop_price = None
    if order_type in ["STOP", "LIMIT"]:
        stop_price = input("Enter the price you would like to set your stop/limit: ")
        try:
            stop_price = float(stop_price)
            if stop_price <= 0:
                print("Stop/Limit price must be a positive number.")
                return
        except ValueError:
            print("Invalid input for stop/limit price. Please enter a valid number.")
            return
    
    # Call create_order with the gathered information
    if action == "BUY":
        if order_type == "MARKET":
            alex_portfolio.create_market_order(ticker, quantity, OrderType.MARKET, OrderAction.BUY)
        elif order_type == "STOP":
            alex_portfolio.create_stop_order(ticker, quantity, OrderType.STOP, OrderAction.BUY, stop_price)
        elif order_type == "LIMIT":
            alex_portfolio.create_limit_order(ticker, quantity, OrderType.LIMIT, OrderAction.BUY, stop_price)
    elif action == "SELL":
        if order_type == "MARKET":
            alex_portfolio.create_market_order(ticker, quantity, OrderType.MARKET, OrderAction.SELL)
        elif order_type == "STOP":
            alex_portfolio.create_stop_order(ticker, quantity, OrderType.STOP, OrderAction.SELL, stop_price)
        elif order_type == "LIMIT":
            alex_portfolio.create_limit_order(ticker, quantity, OrderType.LIMIT, OrderAction.SELL, stop_price)


processor = OrderProcessor(alex_account, alex_portfolio)
processor.start_order_processing_queue()

def signal_handler(sig, frame):
    # Gracefully stop the application when SIGINT (Ctrl+C) is received
    logging.info("Gracefully stopping the application...")
    processor.stop_order_processing_queue()
    exit(0)

if __name__ == "__main__":
    print(".........................Running.........................")
    signal.signal(signal.SIGINT, signal_handler)

    # alex_portfolio.create_limit_order(get_stock("MSFT"), 2, OrderType.LIMIT, OrderAction.BUY, limit=100)
    # alex_portfolio.create_market_order(get_stock("TSLA"), 3, OrderType.MARKET, OrderAction.BUY)

    try:
        while True:
            # This will keep the main thread alive, allowing background threads to run
            if alex_portfolio.pending_orders:
                stock_manager.set_stock_price("DUMMY")
            process_user_input()
            time.sleep(1)
            

    except KeyboardInterrupt:
        logging.info("Application terminated")
    print(".........................End.........................")
    # app.run(debug=True)