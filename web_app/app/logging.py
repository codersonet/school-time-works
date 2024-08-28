import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

# Set up logging configuration
def setup_logging():
    log_file = 'app/logs/app.log'
    if not os.path.exists('app/logs'):
        os.makedirs('app/logs')

    handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

# Log an action
def log_action(action, details):
    logger = setup_logging()
    log_message = f"Action: {action}, Details: {details}, DateTime: {datetime.now()}"
    logger.info(log_message)
  
