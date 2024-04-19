import logging
from colorlog import ColoredFormatter


def logger_config(module):
    """
    Logger function. Extends Python logging module and set a custom config.
    params: Module Name. e.i: logger_config(__name__).
    return: Custom logger_config Object.
    """
  
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)s:     [%(asctime)s]  %(message)s",
        log_colors={
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    custom_logger = logging.getLogger(module)
    custom_logger.setLevel(logging.DEBUG)

    custom_logger.addHandler(handler)

    return custom_logger