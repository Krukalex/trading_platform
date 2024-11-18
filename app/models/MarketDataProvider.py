import yfinance as yf

class MarketDataProvider:
    def __init__(self):
        "Connect to yahoo finance API"
        return
    
    def get_stock_price(self, stock_symbol:str):
        "Retrieve stock prices in real time"
        try:
            stock = yf.Ticker(stock_symbol)
            current_price = stock.info.get("currentPrice")
            
            if current_price is not None:
                return current_price
            else:
                print(f"Price not available for {stock_symbol}.")
                return None
        except Exception as e:
            print(f"Error retrieving stock price for {stock_symbol}: {e}")
            return None
    
    def get_historical_prices(self, stock_symbol:str, start_date:str, end_date:str):
        "Retrieve the price of a stock over a specified time horizon"
        return
    