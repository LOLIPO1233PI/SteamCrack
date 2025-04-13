import logging

Standard_Format = ""  # this totally customizable :)


def create_instance_logger(
    name: str = __name__, level: "logging._Level" = 0
) -> logging.Logger:
    """
    This function handles the creation of loggers to be more easy
    """
    logger = logging.Logger(name, level)
    format = logging.Formatter(Standard_Format)
    logger.setLevel(level)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(format)
    stream_handler.setLevel(level)
    return logger
