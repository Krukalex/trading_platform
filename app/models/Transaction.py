import datetime

class Transaction:
    def __init__(self, amount:float, trans_type:str, fee:float = 0, new_balance:float = 0):
        self.amount = amount
        self.trans_type = trans_type
        self.fee = fee
        self.new_balance = new_balance
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return f"Transaction({self.trans_type}, Amount: {self.amount}, Fee: {self.fee}, New Balance: {self.new_balance})"
