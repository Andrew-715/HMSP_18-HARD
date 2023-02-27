class Config(object):
    DB_NAME: str = 'db_name'
    DB_USER: str = 'db_user'
    DB_PASSWORD: str = 'db_password'
    DB_HOST: str = 'db'
    DB_PORT: str = 5432
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
