from app.models.Stock import Stock
from app.models.MarketDataProvider import MarketDataProvider
import threading

class StockManager:
    def __init__(self, interval = 10):
        self.interval = interval
        self.provider = MarketDataProvider()
        self.stock_dict = {
            "AAPL": Stock("Apple", "AAPL", self.provider.get_stock_price("AAPL")),
            "MSFT": Stock("Microsoft", "MSFT", self.provider.get_stock_price("MSFT")),
            "GOOGL": Stock("Alphabet", "GOOGL", self.provider.get_stock_price("GOOGL")),
            "AMZN": Stock("Amazon", "AMZN", self.provider.get_stock_price("AMZN")),
            "TSLA": Stock("Tesla", "TSLA", self.provider.get_stock_price("TSLA")),
            "META": Stock("Meta Platforms", "META", self.provider.get_stock_price("META")),
            "NFLX": Stock("Netflix", "NFLX", self.provider.get_stock_price("NFLX")),
            "NVDA": Stock("NVIDIA", "NVDA", self.provider.get_stock_price("NVDA")),
            "AMD": Stock("Advanced Micro Devices", "AMD", self.provider.get_stock_price("AMD")),
            "INTC": Stock("Intel", "INTC", self.provider.get_stock_price("INTC")),
            "DUMMY":Stock("Dummy", "Dum", 100)
        }
        self.lock = threading.RLock()

    def get_stock(self, stock_name:str):
        return self.stock_dict[stock_name.upper()]
    
    def update_stock_prices(self, ticker):
        self.stock_dict[ticker].set_price(120)
        return