from urllib.parse import urlencode, quote_plus
import qrcode
import hashlib
import hmac
import base64
import os
from collections import OrderedDict


def get_secret():
    return os.environ['PROTON_DOC_SIGNATURE']


def get_url(payload):
    payload2 = dict()
    base = "https://prod1.protonmexico.com/valida/default/check?"
    for k, v in payload.items():
        payload2[k] = base64.b64encode(bytes(v, 'utf-8')).decode('utf-8')
    return base+urlencode(payload2, quote_via=quote_plus)


def get_signature(payload, secret):
    opayload = OrderedDict(sorted(payload.items()))
    content = "".join(opayload.values())
    signature = base64.b64encode(
        hmac.new(bytes(secret, 'utf-8'), bytes(content, 'utf-8'),
                 digestmod=hashlib.sha256).digest()).decode('utf-8')
    return signature


def save_qr(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img.save(filename)
