# app/security/logger.py

import logging

logging.basicConfig(
    filename="logs/security.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_event(data: dict):
    logging.info(str(data))