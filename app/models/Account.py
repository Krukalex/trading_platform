import uuid
from app.models.Transaction import Transaction

class Account:
    def __init__(self, user):
        from app.models.User import User 
        self.account_id = str(uuid.uuid4())
        self.user_id = user.user_id
        self.balance = 0
        self.fee = None
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

    def deposit(self, amount:float):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)

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
            new_balance = self.get_balance()-(amount+fee)
            self.set_balance(new_balance)

            transaction = Transaction(
                amount=amount,
                trans_type="Withdrawl",
                fee=fee,
                new_balance=self.get_balance()
            )
            self.transaction_history.append(transaction)
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")

    def get_transaction_history(self):
        print(f"Transaction history for {self.user_id}")
        for transaction in self.transaction_history:
            print(transaction)