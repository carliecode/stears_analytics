import logging
import os

def get_logger() -> logging.Logger:
    logger_name = 'stears_analytics_logger'
    logger = logging.getLogger(logger_name)
    if len(logger.handlers) == 0: 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger.setLevel(logging.INFO)
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))
        handler.setFormatter(formatter)    
        logger.addHandler(handler)
    return logger