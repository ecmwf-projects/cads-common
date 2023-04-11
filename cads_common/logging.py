import structlog


def logging_config(config_processors: list):
    structlog.configure(
        processors=config_processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
