from app import app
from app import User

alex = User("Alex", "Alex@example.com")

if __name__ == "__main__":
    print(alex.getUsername())
    print(alex.getEmail())
    print(alex.user_id)
    # app.run(debug=True)