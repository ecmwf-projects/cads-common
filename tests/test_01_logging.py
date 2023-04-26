import logging
import os


def test_logging_configure(level: str = "INFO") -> None:
    # Right level is passed
    level = os.environ["CADS_LOGGING_LEVEL"] = "INFO"
    logging_level = logging.getLevelName(level)
    assert isinstance(logging_level, int) is True
    # Wrong (inexistent) level is passed
    level = "WRONG"
    logging_level = logging.getLevelName(level)
    assert isinstance(logging_level, int) is not True
