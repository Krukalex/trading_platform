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
        self.trade_history = []
        self.order_history = {}

    def get_balance(self):
        return round(self.balance,2)
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
            return False
        else:
            self.add_balance(amount)

            transaction = Transaction(
                amount=amount,
                trans_type="Deposit",
                new_balance=self.get_balance()
            )
            self.transaction_history.append(transaction)
            print(f"Deposited {amount}. New balance: {self.get_balance()}")
            return True
            
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
            return True

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
        fee = round(amount*self.trade_fee_rate,2)
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
        transaction_history_summary = {}
        for trans in self.transaction_history:
            transaction_history_summary[str(trans.trans_id)] = {
                "Type":trans.trans_type,
                "Amount":trans.amount,
                "Fee":trans.fee,
                "New Balance":trans.new_balance,
                "Timestamp":trans.timestamp
            }
        return transaction_history_summary
        
    def get_trade_history(self):
        print(f"Trade history for {self.user_id}")
        trade_history_summary = {}
        for trade in self.trade_history:
            trade_history_summary[str(trade.trade_id)]={
                "Type": trade.trade_type,
                "Stock":trade.stock.ticker,
                "Quantity":trade.quantity,
                "Fee":trade.trade_fee,
                "Cost":trade.cost,
                "New Balance":trade.new_balance,
                "Timestamp": trade.timestamp
            }
        return trade_history_summary
        
    def get_order_history(self):
        print(f"Order history for {self.account_id}")
        order_history_summary = {}
        for order in self.order_history.values():
            order_history_summary[str(order.order_id)] = {
                "Type": str(order.order_type.name),
                "Action": str(order.action.name),
                "Stock": order.stock.ticker,
                "Quantity": order.quantity,
                "Status": str(order.status.name),
                "Created at": order.created_at
            }
        return order_history_summary