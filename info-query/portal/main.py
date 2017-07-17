import os.path
from config import *
from urls import *
import tornado.web
import tornado.httpserver
import tornado.ioloop

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), '../template'),
    static_path=os.path.join(os.path.dirname(__file__), '../static'),
    xsrf_cookies=True,
    debug=True,
    cookie_secret='__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__'
)


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
