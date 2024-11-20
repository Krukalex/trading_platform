from flask import Blueprint, jsonify
from app.models.Account import Account
from app.models.Portfolio import Portfolio
from app.models.User import User
from app.models.StockManager import StockManager

login_blueprint = Blueprint('login', __name__)

