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
