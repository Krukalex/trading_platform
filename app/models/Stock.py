import uuid

class Stock:
    def __init__(self, company_name:str, ticker:str, price:float):
        self.stock_id = uuid.uuid4()
        self.company_name = company_name
        self.ticker = ticker
        self.price = price

    def get_price(self):
        return self.price
    def set_price(self, new_price:float):
        self.price = new_price
    
    def __repr__(self) -> str:
        return f"Stock(company: {self.company_name}, ticker: {self.ticker}, price: {self.price})"