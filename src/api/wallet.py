from flask_restx import Resource, Namespace
import src.functions

WALLET_NS = Namespace('wallets', description='Users namespace')


@WALLET_NS.header('Content-Type', 'application/vnd.api+json')
@WALLET_NS.route('/<string:user_address>')
class WalletsData(Resource):
    def get(self, user_address):
        """Get Wallet Details by User id"""
        data = src.functions.get_wallet_details(user_address)
        data["qr"] = src.functions.generate_qr(user_address)
        return {"data": data}, 200


