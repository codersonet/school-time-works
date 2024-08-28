import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

# Set up logging configuration
def setup_logging():
    log_file = 'app/logs/app.log'
    if not os.path.exists('app/logs'):
        os.makedirs('app/logs')

    handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=5000) # Set a high value of backup count to ensure your old files donget deleted
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

def log_action(action, details):
    logger = logging.getLogger()
    log_message = f"Action: {action} | Details: {details}"
    logger.info(log_message)

# Call setup_logging() to configure logging when module is imported
setup_logging()
