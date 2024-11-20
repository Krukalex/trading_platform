from flask import Blueprint, jsonify
from app.models.Portfolio import Portfolio
from app.models.Account import Account
from stocks import stock_manager

portfolio_blueprint = Blueprint('portfolio', __name__)

account = Account()
portfolio = Portfolio()