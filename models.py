from config import db


class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {"schema": 'public'}

    id = db.Column(db.BigInteger, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=True)
    public_key = db.Column(db.String(1024), nullable=True)
    private_key = db.Column(db.String(1024), nullable=True)


class Wallets(db.Model):
    __tablename__ = 'wallets'
    __table_args__ = {"schema": 'public'}

    id = db.Column(db.BigInteger, nullable=False, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    balance = db.Column(db.BigInteger, nullable=False)
    currency = db.Column(db.String(50), nullable=True, default='Rupees')


class Transactions(db.Model):
    __tablename__ = 'transactions'
    __table_args__ = {"schema": 'public'}

    id = db.Column(db.BigInteger, nullable=False, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.BigInteger, nullable=False)
    recipient_id = db.Column(db.BigInteger, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)
    currency = db.Column(db.String(50), nullable=True, default='Rupees')
    status = db.Column(db.String(50), nullable=True)

