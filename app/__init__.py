from flask import Flask
from app.models.StockManager import StockManager
from app.models.OrderProcessor import OrderProcessor

stock_manager = StockManager()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'my-secret-key-dev'

    # Register Blueprints (routes)
    from .routes.stocks import stock_blueprint
    # from .routes.orders import order_blueprint
    from .routes.login import login_blueprint

    app.register_blueprint(login_blueprint, url_prefix = '/auth')
    app.register_blueprint(stock_blueprint, url_prefix='/stocks')
    # app.register_blueprint(order_blueprint, url_prefix='/orders')

    stock_manager.start_stock_updater()


    return app
