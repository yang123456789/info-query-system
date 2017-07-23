import logging
import tornado.web
from views import *
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
        user = 'select {0} from {1}'.format(username, 'customer')
        ph = 'select {0} from {1}'.format(phone, 'customer')
        if user:
            self.write('username exist')
        if ph:
            self.write('phone exist')
        else:
            return self.do_register(username, cipher_password, phone)

    def do_register(self, username, password, phone):
        if not re.match('[a-zA-Z][a-zA-Z0-9]{3,19}', username):
            self.write('username startswith latter or chinese length 4-20')
        elif not re.match('^1(3|4|5|7|8)\d{9}$', phone):
            self.write('phone Invalid')
        elif not re.match('^(?!^\\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$).{8,20}', password):
            self.write('password contain latter digest special symbol combine 8-20')
        else:
            self.save(username, password, phone)
            self.write('register success')

    def save(self, username, password, phone):
        cipher_password = encrypt_password(password, phone)
        '''insert into (username, password, phone) VALUES (
                {0}, {1}, {2}
                )'''.format(username, cipher_password, phone)

