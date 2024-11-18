from app.models import Stock, MarketDataProvider

provider = MarketDataProvider()

stock_dict = {
    "AAPL": Stock("Apple", "AAPL", provider.get_stock_price("AAPL")),
    "MSFT": Stock("Microsoft", "MSFT", provider.get_stock_price("MSFT")),
    "GOOGL": Stock("Alphabet", "GOOGL", provider.get_stock_price("GOOGL")),
    "AMZN": Stock("Amazon", "AMZN", provider.get_stock_price("AMZN")),
    "TSLA": Stock("Tesla", "TSLA", provider.get_stock_price("TSLA")),
    "META": Stock("Meta Platforms", "META", provider.get_stock_price("META")),
    "NFLX": Stock("Netflix", "NFLX", provider.get_stock_price("NFLX")),
    "NVDA": Stock("NVIDIA", "NVDA", provider.get_stock_price("NVDA")),
    "AMD": Stock("Advanced Micro Devices", "AMD", provider.get_stock_price("AMD")),
    "INTC": Stock("Intel", "INTC", provider.get_stock_price("INTC"))
}
