import logging
import os
from datetime import datetime

def get_logger(name="pipeline", level="INFO", log_dir="logs"):
    """
    Creates and returns a configured logger with both console and file output.
    Ensures no duplicate handlers get created.
    """

    # Convert level string → logging level
    level = getattr(logging, level.upper(), logging.INFO)

    # Ensure log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Log file path
    log_file = os.path.join(
        log_dir,
        f"{name}_{datetime.now().strftime('%Y-%m-%d')}.log"
    )

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding handlers twice
    if not logger.handlers:

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%H:%M:%S"
        ))

        # File handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ))

        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger


