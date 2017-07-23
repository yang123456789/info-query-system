from tornado.options import define, options


define('port', default=8080, type=int, help='server listening port')
define('mysql_host', default='127.0.0.1:3306', help='mysql host and default port')
define('mysql_db', default='information', help='mysql database')
define('mysql_user', default='root', help='mysql user')
define('mysql_password', default='123456789', help='mysql password')
define('mongodb_db', default='', help='mongodb database')
define('mongodb_user', default='', help='mongodb user')
define('mongodb_password', default='', help='mongodb password')
define('mongodb_host', default='127.0.0.1:27017', help='mongodb host and default port')

# RSA
SECRET = {
    'public_key': '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCbvcSgE2OwvkabU0taExApPzGf
KQmtGeBZllHNLI6Xxax0X2nN5sY5H0+dVYPKPQeNAhJu7jNGgqBigC52V037lk23
eQ/6O9dvva/WzawLo7t7y2kic/EwjRI0EZ0YQcUcEaylUCzxHWg+dM05fPEjtLNf
K4bKrbGk7K+hSk7KNQIDAQAB
-----END PUBLIC KEY-----''',
    'private_key': '''-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCbvcSgE2OwvkabU0taExApPzGfKQmtGeBZllHNLI6Xxax0X2nN
5sY5H0+dVYPKPQeNAhJu7jNGgqBigC52V037lk23eQ/6O9dvva/WzawLo7t7y2ki
c/EwjRI0EZ0YQcUcEaylUCzxHWg+dM05fPEjtLNfK4bKrbGk7K+hSk7KNQIDAQAB
AoGAZfRCPyTSU0cNA+vwXUQzhT0IaBA+dGKHOz6ryGxN4M+YSQqZQiC8TXLQ9Meh
ogh34/iiRpqLWLJ0+ma9g909f9sxeOb1Jc1Zl0ip5/EHvySyV1GGXF+izPvOss0j
4I4+iWyhjbJQMGIknEV6HGQFx85UCOH9MNuFGS4k96wT/wECQQC+A5rXSKDuMbjI
3cP7GSuDIkgM4AD/ndUMQ5peTqztycUskf1ahoU5+aEF4blM2jVffQbxZX2WNVLY
V1jk6Q31AkEA0dNJE8JR9Hyg4hC6lW0iLcbLpUwhlGiq7PKsRUD7xnUIB13Rb8a7
+Y02BQKhIW2Bp/sUY4Ekp8vqYOBFSXrjQQJBAJQ2HZ4VAaop0HelO0vt6xnDMK4S
P9UimF6TkKJE/fAQdSL50MO+r8Zz51y+H5pJjl4oGLVMM7RpbXBgWW9cNc0CQEP8
lPodBZcVZr+5MevG38M7XbLilyLSQ0fhXaZW5v2n4AEbCgiQuUmj0rQO5QzCwbcf
KL0RFEJ2VSwsnuavNcECQF9Na0ra3dggGJP2Rk5l6EK6O7SN09RZb8RdfIAYTyOt
vjbqCdyhnW61AkhLitvjSszUWm4YRjnMDb6Q1sjSJm0=
-----END RSA PRIVATE KEY-----'''
}
