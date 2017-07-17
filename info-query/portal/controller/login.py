import logging
import tornado.web


class IndexHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class LoginUP(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html')
