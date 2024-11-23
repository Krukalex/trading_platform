from flask import Blueprint, jsonify
from app import stock_manager

stock_blueprint = Blueprint("stocks", __name__)

@stock_blueprint.route('/')
def get_all_stocks():
    stocks = stock_manager.stock_dict
    stocks = {ticker: {"Company": stock.company_name, "Price":stock.get_price()} for ticker, stock in stock_manager.stock_dict.items()}
    return jsonify(stocks)

@stock_blueprint.route('/<ticker>')
def get_stock(ticker):
    try:
        stock = stock_manager.get_stock(ticker)
        return jsonify({
            "ticker": stock.ticker,
            "company_name": stock.company_name,
            "price": stock.price
        })
    except KeyError:
        return jsonify({"error": "Stock not found"}), 404