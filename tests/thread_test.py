import threading
import time

stock_dict = {
    "AAPL": 100,
    "MSFT": 140,
    "AMZN": 200
}

def process_queue():
    if stock_dict["AAPL"]>150:
        print("buying apple!")
    else:
        print("price is not high enough")

def start_order_queue_processor(interval = 10):
    def run_processor():
        process_queue()
        threading.Timer(interval, run_processor).start()

    run_processor()

def update_stock():
    stock_dict["AAPL"] = 200

def start_stock_updater(interval = 30):
    def run_updater():
        update_stock()
        threading.Timer(interval, run_updater).start()
    run_updater()


start_order_queue_processor()
time.sleep(20)
start_stock_updater()