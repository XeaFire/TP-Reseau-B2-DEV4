from enum import Enum
from datetime import datetime
from re import compile as recompile
from sys import exit as sysexit, argv
from os import mkdir, path, access, W_OK


TEMP_DIR = "/tmp"
LOG_DIR = f"{TEMP_DIR}/network_tp3"
LOG_FILE = f"{LOG_DIR}/network.log"


def create_log_dir() -> bool:
    """Creates LOG_DIR and checks if LOG_FILE is writable"""
    if not path.exists(LOG_DIR):
        try:
            mkdir(LOG_DIR)
        except Exception:
            print(f"Could not create log directory {LOG_DIR}.")
            sysexit(2)

    if not access(LOG_DIR, W_OK):
        print(f"Can't write to log file {LOG_FILE}.")
        sysexit(3)

    return True


class LogLevel(Enum):
    """Simple log level enums"""

    INFO = 1
    ERROR = 2


def log(msg: str, log_level: LogLevel) -> True:
    """Writes given msg to LOG_FILE adding a timestamp"""
    # on récupère un timestamp au bon format pour la ligne de log
    log_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # construction de la ligne de log
    log_line = f"{log_timestamp} [{log_level.name}] {msg}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line)

    return True
