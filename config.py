class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_HASH_SALT = b'HfdsfsnmDRsds1!834'
    PWD_HASH_ITERATIONS = 100_000
    JWT_ALGO = 'HS256'
    JWT_SECRET = 's3cR3t'
    ITEMS_ON_PAGE = 12
