from flask import Blueprint, jsonify, request, session
from app.models.Portfolio import Portfolio
from app.models.OrderProcessor import OrderProcessor
from data.mock_db import user_db, account_db
from app import stock_manager

login_blueprint = Blueprint('login', __name__)

active_order_processors = {}
active_portfolios = {}
active_account = {}

@login_blueprint.route('/login', methods=['POST'])
def login():
    try:
        # Safely get the JSON data
        data = request.get_json()
        
        # Check if JSON was provided
        if not data:
            return jsonify({"error": "Invalid request, JSON payload is required"}), 400
        
        # Check if the username key exists
        username = data.get("username")
        if not username or username not in user_db:
            return jsonify({"error": "Invalid username"}), 400

        # Retrieve user and account
        user = user_db[username]
        account = account_db.get(user.user_id)
        if not account:
            return jsonify({"error": "Account not found for user"}), 404
        
        active_account[user.user_id] = account

        # Create portfolio and start order processing
        portfolio = Portfolio(account, stock_manager)
        active_portfolios[user.user_id] = portfolio
        order_processor = OrderProcessor(account, portfolio)
        order_processor.start_order_processing_queue()
        active_order_processors[user.user_id] = order_processor

        # Store user info in session
        session['user_id'] = user.user_id
        session['username'] = user.username

        return jsonify({"message": f"Welcome, {user.username}!"}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


@login_blueprint.route('/logout', methods = ['POST'])
def logout():
    user_id = session.pop(user_id, None)
    if user_id and user_id in active_order_processors:
        # Stop the user's OrderProcessor
        active_order_processors[user_id].stop_order_processing_queue()
        del active_order_processors[user_id]

    session.clear()
    return jsonify({"message": "Logged out successfully!"}), 200