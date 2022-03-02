from src.api.users import USER_NS
from src.api.wallet import WALLET_NS
from src.api.payment import PAYMENT_NS
from src.db import db
from flask import Blueprint
from flask_restx import Api
from flask import Flask, render_template


def create_app(app_settings):
    """
        Enter context point for the application
    """
    app = Flask(__name__)
    app.config.from_object(app_settings)

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/wallets")
    def wallets():
        return render_template('view_wallet.html')

    @app.route("/transactions")
    def transactions():
        return render_template('make_transaction.html')

    API_BLUEPRINT = Blueprint("api", __name__, url_prefix="/api/v1")

    api = Api(
        API_BLUEPRINT,
        default="Blockchain API",
        version="1.0",
        title="Blockchain API",
        description="Blockchain API",
    )
    app.register_blueprint(API_BLUEPRINT)
    db.init_app(app)
    api.add_namespace(WALLET_NS)
    api.add_namespace(USER_NS)
    api.add_namespace(PAYMENT_NS)

    return app
