from app.models import User, Account

alex = User("Alex", "Alex@example.com")
alex_account = Account(alex)

if __name__ == "__main__":
    print(alex.getUsername())
    print(alex.getEmail())
    print(f"User ID: {alex.user_id}")
    print(f"Account ID: {alex_account.account_id}")
    print(f"User ID for account: {alex_account.user_id}")
    print(f"Alex has an account with ID: {alex.account_id}")
    # app.run(debug=True)