import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/mfare'
=======
    SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_BROWN_URL')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dk:Dennisveer27@localhost/mfare'
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee

    DEBUG = True


class TestConfig(Config):
<<<<<<< HEAD
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/mfare'
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dk:Dennisveer27@localhost/mfare_tests'
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dk:Dennisveer27@localhost/mfare_tests'
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig,
}
