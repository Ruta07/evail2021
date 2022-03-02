from blockcypher import generate_new_address, create_wallet_from_address, get_address_overview
from blockcypher import send_faucet_coins, simple_spend
import qrcode

api_token = '05894c026f1c489685410dfad7f44c45'


def create_public_private_keys():
    return generate_new_address(coin_symbol='bcy', api_key=api_token)


def create_wallet(data, keys):
    return create_wallet_from_address(wallet_name=data["name"], address=keys, api_key=api_token, coin_symbol='bcy')


def get_wallet_details(address):
    return get_address_overview(address=address, coin_symbol='bcy', api_key=api_token)


def add_faucet(address, amount):
    return send_faucet_coins(address_to_fund=address, satoshis=amount, coin_symbol='bcy', api_key=api_token)


def send_payment(from_address, to_address, amount):
    return simple_spend(from_privkey=from_address, to_address=to_address, to_satoshis=amount, api_key=api_token, coin_symbol='bcy')


def generate_qr(user_address):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(user_address)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")
    path = "C:\\eval_2021\\blockchain\\static\\qr\\" + user_address + ".png"
    img.save(path)
    return path
