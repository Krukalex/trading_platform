from app.models.User import User
from app.models.Account import Account

user_db = {}
account_db = {}

user1 = User("user1", "user1@example.com")
user2 = User("user2", "user2@example.com")
user3 = User("user3", "user3@example.com")

user_db[user1.username] = user1
user_db[user2.username] = user2
user_db[user3.username] = user3

account1 = Account(user1)
account2 = Account(user2)
account3 = Account(user3)

account_db[user1.user_id] = account1
account_db[user2.user_id] = account2
account_db[user3.user_id] = account3