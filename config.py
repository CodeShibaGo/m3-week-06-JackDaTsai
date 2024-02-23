import os
from dotenv import load_dotenv

class Config:
    load_dotenv()

    host = os.getenv("host")
    user = os.getenv("user")
    password = os.getenv("password")
    database = os.getenv("database")
    port = os.getenv("port")

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
