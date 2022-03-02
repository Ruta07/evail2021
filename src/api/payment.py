from flask_restx import Resource, Namespace
import src.functions
from flask import request
from src.database.models import Transactions
from src.db import db

PAYMENT_NS = Namespace('payment', description='Payment namespace')


@PAYMENT_NS.header('Content-Type', 'application/vnd.api+json')
@PAYMENT_NS.route('/<string:user_address>')
class PaymentData(Resource):
    def get(self, user_address):
        """Get Wallet Details by User id"""
        data = src.functions.get_wallet_details(user_address)
        return {"data": data}, 200


@PAYMENT_NS.header('Content-Type', 'application/vnd.api+json')
@PAYMENT_NS.route('/create')
class CreatePayment(Resource):
    def post(self):
        """Make payment"""
        input_data = {"sender_private_key": request.form["from_address"],
                      "recipient_address": request.form["to_address"],
                      "amount": int(request.form["amount"]),
                      }
        data = src.functions.send_payment(input_data["sender_private_key"], input_data["recipient_address"], input_data["amount"])
        if "error" in data:
            return "Wallet Creation Failed", 500
        try:
            new_transc = Transactions(**input_data)
            db.session.add(new_transc)
            db.session.commit()
            return {"data": data}, 200
        except SystemExit:
            return {'errors': [{'detail': 'High level error during creation of user'}]}, 422


@PAYMENT_NS.header('Content-Type', 'application/vnd.api+json')
@PAYMENT_NS.route('/faucet')
class FaucetPayment(Resource):
    def post(self):
        """Make faucet payment"""
        to_address = request.form["to_address"]
        amount = int(request.form["amount"])
        data = src.functions.add_faucet(to_address, amount)
        return {"data": data}, 200

