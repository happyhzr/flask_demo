from datetime import timedelta
from os import urandom

DEBUG = True

SECRET_KEY = urandom(24)
# SECRET_KEY = 'Keyborad Cat'
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'Password.123456'
HOST = '45.63.52.242'
PORT = 3306
DATABASE = 'test'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
