from functools import wraps
from config import SECRET
import json
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import hashlib


def render_200(data, status=200):
    data = json.dumps({'status': status, 'message': data})
    return data


def render_400(data, status=400):
    data = json.dumps({'status': status, 'message': data})
    return data


def render_404(data, status=404):
    data = json.dumps({'status': status, 'message': data})
    return data


def render_409(data, status=409):
    data = json.dumps({'status': status, 'message': data})
    return data


def render_500(data, status=500):
    data = json.dumps({'status': status, 'message': data})
    return data


def render_json(data):
    data = json.dumps({'message': data})
    return data


def decrypt_password(secret_key):
    private_key = SECRET['private_key']
    rsa_key = RSA.importKey(private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    password = cipher.decrypt(base64.b64decode(secret_key), '')
    return password


def encrypt_password(password, phone):
    first = base64.b64encode(phone)[:-2]
    last = hashlib.md5(password).hexdigest()
    cipher_password = first.join(last)
    return cipher_password
