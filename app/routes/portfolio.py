from flask import Blueprint, jsonify, session, request
from app.models.Order import OrderType, OrderAction
from app.models.Portfolio import Portfolio
from app.models.Account import Account
# from stocks import stock_manager
from .login import active_portfolios

portfolio_blueprint = Blueprint('portfolio', __name__)

@portfolio_blueprint.route('/holdings', methods = ['GET'])
def get_holdings():
    holdings = active_portfolios[session['user_id']].get_holdings()
    return jsonify(holdings)

@portfolio_blueprint.route('/buy_market_order', methods = ['POST'])
def buy_market_order():
    user_id = session["user_id"]
    if not user_id:
        return jsonify({"error": "User not logged in"}), 403
    
    portfolio = active_portfolios[user_id]
    if not portfolio:
        return jsonify({"error": "Portfolio not found"}), 404

    data = request.json

    ticker = data["ticker"]
    quantity = data["quantity"]
    order_type = OrderType.MARKET
    action = OrderAction.BUY

    if not ticker or not quantity or not order_type or not action:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        success = portfolio.create_market_order(ticker, quantity, order_type, action)
        print(success)
        if success:
            return jsonify({"message": f"Market order to {action.name.lower()} {quantity} shares of {ticker} created successfully."}), 200
        else:
            return jsonify({"message": f"Insufficient funds"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@portfolio_blueprint.route('/sell_market_order', methods = ['POST'])
def sell_market_order():
    user_id = session["user_id"]
    if not user_id:
        return jsonify({"error": "User not logged in"}), 403
    
    portfolio = active_portfolios[user_id]
    if not portfolio:
        return jsonify({"error": "Portfolio not found"}), 404

    data = request.json

    ticker = data["ticker"]
    quantity = data["quantity"]
    order_type = OrderType.MARKET
    action = OrderAction.SELL

    if not ticker or not quantity or not order_type or not action:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        success = portfolio.create_market_order(ticker, quantity, order_type, action)
        print(success)
        if success:
            return jsonify({"message": f"Market order to {action.name.lower()} {quantity} shares of {ticker} created successfully."}), 200
        else:
            return jsonify({"message": f"Can't sell {quantity} shares of {ticker}. You currently own {portfolio.holdings[ticker]['quantity']} shares."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500