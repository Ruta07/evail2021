from src.db import db


class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {"schema": 'public'}

    id = db.Column(db.BigInteger, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=True)
    public_key = db.Column(db.String(1024), nullable=True)
    private_key = db.Column(db.String(1024), nullable=True)
    address = db.Column(db.String(1024), nullable=True)


class Wallets(db.Model):
    __tablename__ = 'wallets'
    __table_args__ = {"schema": 'public'}

    id = db.Column(db.BigInteger, nullable=False, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    total_received = db.Column(db.BigInteger, nullable=True)
    total_sent = db.Column(db.BigInteger, nullable=True)
    balance = db.Column(db.BigInteger, nullable=True)
    unconfirmed_balance = db.Column(db.BigInteger, nullable=True)
    final_balance = db.Column(db.BigInteger, nullable=True)


class Transactions(db.Model):
    __tablename__ = 'transactions'
    __table_args__ = {"schema": 'public'}

    id = db.Column(db.BigInteger, nullable=False, primary_key=True, autoincrement=True)
    sender_private_key = db.Column(db.String(1024), nullable=False)
    recipient_address = db.Column(db.String(1024), nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)


