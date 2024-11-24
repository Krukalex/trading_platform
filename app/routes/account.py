from flask import Blueprint, jsonify, request, session
from .login import active_account

account_blueprint = Blueprint("account", __name__)

@account_blueprint.route('balance', methods = ["GET"])
def get_balance():
    user_id = session["user_id"]
    account = active_account[user_id]
    return jsonify({"message": f"Account balance is {account.get_balance()}"})

@account_blueprint.route('deposit', methods = ["POST"])
def deposit():
    user_id = session["user_id"]
    if not user_id:
        return jsonify({"error": "User not logged in"}), 403
    if user_id not in active_account:
        return jsonify({"error":f"Need to sign in as a valid user. {user_id} is not a valid user"})

    account = active_account[user_id]

    data = request.json
    amount = data["amount"]

    try:
        amount = float(amount)
    except:
        return jsonify({"Error": "Amount must be a number"})
    
    if account.deposit(amount):
        return jsonify({"message": f"successfully deposited {amount} into your account!"})
    else:
        return jsonify({"message": "error depositing into account"})

@account_blueprint.route('withdraw', methods = ["POST"])
def withdraw():
    user_id = session["user_id"]
    if not user_id:
        return jsonify({"error": "User not logged in"}), 403
    if user_id not in active_account:
        return jsonify({"error":f"Need to sign in as a valid user. {user_id} is not a valid user"})
    
    account = active_account[user_id]

    data = request.json
    amount = data["amount"]

    try:
        amount = float(amount)
    except:
        return jsonify({"Error": "Amount must be a number"})
    
    if account.withdraw(amount):
        return jsonify({"message": f"successfully withdrew {amount} into your account!"})
    else:
        return jsonify({"message": "error withdrawing from account"})
    
    
@account_blueprint.route("transaction_history", methods = ["GET"])
def get_transaction_history():
    user_id = session["user_id"]
    if not user_id:
        return jsonify({"error": "User not logged in"}), 403
    if user_id not in active_account:
        return jsonify({"error":f"Need to sign in as a valid user. {user_id} is not a valid user"})
    
    account = active_account[user_id]

    try:
        return jsonify(account.get_transaction_history())
    except:
        return jsonify({"message": "error retrieving transaction history"})
    

@account_blueprint.route("trade_history", methods = ["GET"])
def get_trade_history():
    user_id = session["user_id"]
    if not user_id:
        return jsonify({"error": "User not logged in"}), 403
    if user_id not in active_account:
        return jsonify({"error":f"Need to sign in as a valid user. {user_id} is not a valid user"})
    
    account = active_account[user_id]

    try:
        return jsonify(account.get_trade_history())
    except:
        return jsonify({"message": "error retrieving trade history"})


@account_blueprint.route("order_history", methods = ["GET"])
def get_order_history():
    user_id = session["user_id"]
    if not user_id:
        return jsonify({"error": "User not logged in"}), 403
    if user_id not in active_account:
        return jsonify({"error":f"Need to sign in as a valid user. {user_id} is not a valid user"})
    
    account = active_account[user_id]

    try:
        return jsonify(account.get_order_history())
    except:
        return jsonify({"message": "error retrieving order history"})