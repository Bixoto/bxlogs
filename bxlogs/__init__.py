import os
from typing import Optional, Union, Type
import logging

__version__ = '0.1.0'
__all__ = [
    '__version__',
    'DEFAULT_LEVEL', 'ENV_VAR',
    'get_logger',
]

DEFAULT_LEVEL = logging.INFO
ENV_VAR = "BX_DEBUG"


def get_logger(name: str, *,
               debug: Optional[bool] = None,
               level: Optional[Union[int, str]] = None,
               handler_class: Type[logging.Handler] = logging.StreamHandler):
    """
    Return a logger with the given name.

    Create a logger with the given level or the default one, and add it a stream handler (`sys.stderr`).

    :param name: logger name passed to `logging.getLogger`
    :param debug: if True, default the level to `DEBUG`
    :param level: if set, use it as the level. This takes precedence over `debug`.
    :param handler_class: set the handler class. This is used for tests
    """
    logger = logging.getLogger(name)

    if level is None:
        if debug is None:
            debug_env = os.environ.get(ENV_VAR)
            if debug_env is not None:
                debug = debug_env == "1"

        if debug:
            level = logging.DEBUG

    if level is None:
        level = DEFAULT_LEVEL

    logger.setLevel(level)

    formatter = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = handler_class()
    handler.setFormatter(formatter)

    # Remove any existing handler
    if logger.handlers:
        n = len(logger.handlers)
        logging.warning("Logger %r has already %s handler%s." % (name, n, "s" if n > 1 else ""))

    logger.addHandler(handler)
    return logger
