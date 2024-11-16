from app.models import User, Account, Portfolio, Stock
from app.models.Order import OrderAction, OrderType
from app.models.OrderProcessor import OrderProcessor

alex = User("Alex", "Alex@example.com")
alex_account = Account(alex)

mike = User("Mike", "Mike@example.com")
mike_account = Account(mike)

alex_portfolio = Portfolio(alex_account)

aapl = Stock("Apple", "AAPL", 100)
msft = Stock("Microsoft", "MSFT", 120)

processor = OrderProcessor(alex_account, alex_portfolio)
processor.procces_order_queue()

if __name__ == "__main__":
    print(".........................Running.........................")


    alex_portfolio.create_stop_order(msft, 2, OrderType.STOP, OrderAction.BUY, stop=140)

    print(".........................End.........................")
    # app.run(debug=True)