import json
import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

_logger = logging.getLogger("secure_agent.security")
_logger.setLevel(logging.INFO)

if not _logger.handlers:
    _handler = logging.FileHandler("logs/security.log", encoding="utf-8")
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    _logger.addHandler(_handler)


def log_event(data: dict) -> None:
    """Write a structured JSON entry to the security log for every UNSAFE decision."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        **data,
    }
    _logger.info(json.dumps(entry))
