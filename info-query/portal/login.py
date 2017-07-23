import logging
import tornado.web
from views import *
from mysql import *
import re


class IndexHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class Register(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html')

    def post(self, *args, **kwargs):
        username = self.get_body_argument('username', None)
        password = self.get_body_argument('password', None)
        phone = self.get_body_argument('phone', None)
        cipher_password = decrypt_password(password)
        pw = encrypt_password(cipher_password, phone)
        if not re.match('^[a-zA-Z][a-zA-Z0-9]{3,19}$', username):
            self.write('username must be startswith latter and endswith alpha length 4-20')
        elif not re.match('^(?!^\\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$).{8,20}', password):
            self.write('password must be alphanumeric special symbol and length 8-20')
        elif not re.match('^1(3|4|5|7|8)\d{9}$', phone):
            self.write('phone invalid')
        else:
            self.save(username, cipher_password, phone)
            self.write(200)

    def save(self, username, password, phone):
        statement = '''INSERT INTO customer (username, password, phone) VALUES (
                    {0}, {1}, {2}
                    )'''.format(username, password, phone)
        operation = Operation()
        operation.create(statement)
