from flask import Blueprint, jsonify, request, session
from .login import active_account

account_blueprint = Blueprint("account", __name__)

@account_blueprint.route('balance', methods = ["GET"])
def get_balance():
    user_id = session["user_id"]
    account = active_account[user_id]
    return jsonify({"message": f"Account balance is {account.get_balance()}"})

@account_blueprint.route('add_balance', methods = ["POST"])
def add_balance():
    user_id = session["user_id"]

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