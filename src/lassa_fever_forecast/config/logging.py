import sys

from loguru import logger

logger.remove()

logger.add(
    sys.stderr,
    level="INFO",
    colorize=True,
    backtrace=True,
    diagnose=False,
)

logger.add(
    "logs/project.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)
