import os
from dotenv import load_dotenv

class Config:
    load_dotenv()

    user = os.getenv("user")
    password = os.getenv("password")
    database = os.getenv("database")
    port = os.getenv("port")

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"mysql+pymysql://{user}:{password}@localhost:{port}/{database}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_PORT = int(os.getenv("MAIL_PORT"))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']