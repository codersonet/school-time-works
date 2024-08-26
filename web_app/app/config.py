# app/config.py
import os

class Config:
    # Use the environment variable if set, otherwise default to a secure key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_generated_secret_key_here')
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '1234'
    DATABASE = 'dsb'
