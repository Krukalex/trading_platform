from app.models import User, Account

alex = User("Alex", "Alex@example.com")
alex_account = Account(alex)

mike = User("Mike", "Mike@example.com")
mike_account = Account(mike)

if __name__ == "__main__":
    print(alex.get_username())
    print(alex.get_email())
    print(f"User ID: {alex.user_id}")
    print(f"Account ID: {alex_account.account_id}")
    print(f"User ID for account: {alex_account.user_id}")
    print(f"Alex has an account with ID: {alex.account_id}")

    alex_account.deposit(100)
    alex_account.deposit(200)

    alex_account.withdraw(500)
    alex_account.withdraw(200)
    alex_account.withdraw(100)

    alex_account.transfer(mike_account, 50)

    print(mike_account.get_balance())


    alex_account.get_transaction_history()

    mike_account.get_transaction_history()
    # app.run(debug=True)