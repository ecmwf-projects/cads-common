import logging
import os
import sys

import structlog


def structlog_configure(additional_processors: list = []):
    """Configure structlog logging."""
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
            *additional_processors,
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


def logging_configure(level: str = "INFO") -> None:
    """Configure the logging basic config."""
    level = os.getenv("CADS_LOGGING_LEVEL", level)
    logging_level = logging.getLevelName(level)
    if not isinstance(logging_level, int):
        logging_level = logging.INFO
    logging.basicConfig(
        level=logging_level,
        format="%(message)s",
        stream=sys.stdout,
    )
