import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
from flask import jsonify
import binascii
from config import db
from models import Users


def generate_wallet():
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.public_key()
    keys = {
        'private_key': binascii.hexlify(private_key.exportKey(format('DER'))).decode('ascii'),
        'public_key': binascii.hexlify(public_key.exportKey(format('DER'))).decode('ascii')
    }
    return jsonify(keys)


def get_users():
    result = db.session.query(Users).all()
    data = []
    for user in result:
        item = {"id": user.id, "name": user.name, "public_key": user.public_key}
        data.append(item)
    return {"data": data}


def save_user(sender_public_key, sender_private_key, name):
    user = Users(sender_public_key=sender_public_key, sender_private_key=sender_private_key, name=name)
    db.session.add(user)
    db.session.commit()
    return {"message": "User Saved"}



