import uuid
from app.models.Transaction import Transaction

class Account:
    def __init__(self, user):
        from app.models.User import User 
        self.account_id = str(uuid.uuid4())
        self.user_id = user.user_id
        self.balance = 0
        self.trade_fee_rate = 0.01
        user.link_account(self)
        self.transaction_history = []

    def get_balance(self):
        return self.balance
    def set_balance(self, amount:float):
        if amount<0:
            print("Amount cannot be negative")
        self.balance = amount
    def get_account_id(self):
        return self.account_id
    def get_user_id(self):
        return self.user_id
    
    def add_balance(self, amount:float):
        self.balance+=amount
    def deduct_balance(self, amount:float):
        self.balance-=amount


    def deposit(self, amount:float):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.add_balance(amount)

            transaction = Transaction(
                amount=amount,
                trans_type="Deposit",
                new_balance=self.get_balance()
            )
            self.transaction_history.append(transaction)
            print(f"Deposited {amount}. New balance: {self.get_balance()}")
            
    def withdraw(self, amount:float, fee:float = 2):
        if (amount+fee)>self.get_balance():
            print("Can't withdraw amount higher than current balance")
        else:
            self.deduct_balance((amount+fee))

            transaction = Transaction(
                amount=amount,
                trans_type="Withdrawal",
                fee=fee,
                new_balance=self.get_balance()
            )
            self.transaction_history.append(transaction)
            print(f"Withdrew {amount}. Fee of {fee} was deducted. New balance: {self.get_balance()}")

    def transfer(self, destination:"Account", amount:float, fee:float = 2):
        if (amount+fee)>self.get_balance():
            print(f"Attempting to transfer an amount greater than the account balance. You have a balance of {self.get_balance()}")
        else:
            self.deduct_balance((amount+fee))

            transaction_source = Transaction(
                amount = amount,
                trans_type = "Transfer",
                fee = fee,
                new_balance=self.get_balance()
            )

            self.transaction_history.append(transaction_source)

            destination.add_balance(amount)

            transaction_destination = Transaction(
                amount=amount,
                trans_type="Received Transfer",
                fee = 0,
                new_balance=destination.get_balance()
            )

            destination.transaction_history.append(transaction_destination)
            print(f"Transfered {amount}. Fee of {fee} was deducted. New balance: {self.get_balance()}.")
            print(f"Transfer was received for the amount {amount}. New balance is {destination.get_balance()}")

    def apply_trade_fee(self, amount:float):
        fee = amount*self.trade_fee_rate
        self.deduct_balance(fee)

        transaction = Transaction(
            amount=fee,
            trans_type="Trade Fee",
            new_balance=self.get_balance()
        )
        self.transaction_history.append(transaction)
        print(f"Trade fee applied for the amount of {fee}. New balance is {self.get_balance()}")


    def get_transaction_history(self):
        print(f"Transaction history for {self.user_id}")
        for transaction in self.transaction_history:
            print(transaction)