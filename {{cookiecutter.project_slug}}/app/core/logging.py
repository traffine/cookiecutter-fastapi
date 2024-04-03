import datetime
import logging
import sys

from core.config import LOGGING_LEVEL
from pythonjsonlogger import jsonlogger
from pytz import timezone


class JsonFormatter(jsonlogger.JsonFormatter):
    def parse(self):
        return [
            "process",
            "timestamp",
            "level",
            "name",
            "message",
            "stack_info",
        ]

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.datetime.now(timezone("Asia/Tokyo")).strftime("%Y-%m-%dT%H:%M:%S%z")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


def getLogger(module_name):
    logger = logging.getLogger(module_name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = JsonFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(LOGGING_LEVEL)
    return logger
