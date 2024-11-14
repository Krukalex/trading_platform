from app.models import User, Account, Portfolio, Stock

alex = User("Alex", "Alex@example.com")
alex_account = Account(alex)

mike = User("Mike", "Mike@example.com")
mike_account = Account(mike)

alex_portfolio = Portfolio(alex_account)

aapl = Stock("Apple", "AAPL", 100)
msft = Stock("Microsoft", "MSFT", 120)

if __name__ == "__main__":
    print(".........................Running.........................")
    # alex_account.deposit(100)
    # alex_account.deposit(200)

    # alex_account.withdraw(500)
    # alex_account.withdraw(200)
    # alex_account.withdraw(100)

    # alex_account.transfer(mike_account, 50)

    # print(mike_account.get_balance())


    # alex_account.get_transaction_history()

    # mike_account.get_transaction_history()

    # alex_portfolio.buy_stock(aapl, 5)

    alex_account.deposit(1000)

    # alex_portfolio.buy_stock(aapl, 2)
    alex_portfolio.buy_stock(msft, 4)

    # alex_portfolio.get_holdings()

    # alex_account.get_transaction_history()
    # alex_account.get_trade_history()

    # alex_portfolio.sell_stock(msft, 6)
    # alex_portfolio.sell_stock(msft, 2)

    alex_portfolio.create_order(msft, 2, "market order", "sell")
    alex_portfolio.get_holdings()
    alex_account.get_trade_history()
    alex_account.get_order_history()
    print(".........................End.........................")
    # app.run(debug=True)