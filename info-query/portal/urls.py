from controller.login import *


handlers = [
    (r'/', IndexHander),
    (r'/register', LoginUP),
]
