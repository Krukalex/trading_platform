from app.models.User import User
from app.models.Account import Account
from app.models.Portfolio import Portfolio

user_db = {}
account_db = {}
portfolio_db = {}

user1 = User("user1", "user1@example.com")
user2 = User("user2", "user2@example.com")
user3 = User("user3", "user3@example.com")

account1 = Account(user1)
account2 = Account(user2)
account3 = Account(user3)

portolio1 = Portfolio(account1)