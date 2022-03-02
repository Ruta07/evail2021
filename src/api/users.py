"""
User resource for managing the wallet Users
"""
from flask import request
from flask_restx import Resource, Namespace
from src.db import db
from src.database.models import Users
import src.functions


USER_NS = Namespace('users', description='Users namespace')


@USER_NS.header('Content-Type', 'application/vnd.api+json')
@USER_NS.route('')
class UserData(Resource):
    def post(self):
        """Create new User"""
        try:
            input_data = {"name": request.form["user_name"]}
            keys = src.functions.create_public_private_keys()
            input_data["public_key"] = keys["public"]
            input_data["private_key"] = keys["private"]
            input_data["address"] = keys["address"]
            data = src.functions.create_wallet(input_data, keys["address"])
            if "error" in data:
                return "Wallet Creation Failed", 500
            new_user = Users(**input_data)
            db.session.add(new_user)
            db.session.commit()
            return data, 200
        except SystemExit:
            return {'errors': [{'detail': 'High level error during creation of user'}]}, 422

    def get(self):
        """Get Users"""
        data = {}
        data_list = []
        result = db.session.query(Users).all()
        for user in result:
            data["name"] = user.name
            data["address"] = user.address
            data["private_address"] = user.private_key
            user_data = data.copy()
            data_list.append(user_data)
        return {"data": data_list}, 200