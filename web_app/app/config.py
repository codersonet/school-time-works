# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')  # Use the secret key from the .env file
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '1234'
    DATABASE = 'dsb'
