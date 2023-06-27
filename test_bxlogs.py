import logging
import os
from logging import StreamHandler

import pytest

from bxlogs import get_logger, ENV_VAR, DEFAULT_LEVEL


class FakeHandler(StreamHandler):
    def __init__(self):
        super().__init__()
        self.msgs = []

    def emit(self, record):
        msg = self.format(record)
        self.msgs.append(msg)


@pytest.fixture()
def env_debug():
    previous = os.environ.get(ENV_VAR)
    os.environ[ENV_VAR] = "1"
    yield
    if previous is None:
        del os.environ[ENV_VAR]
    else:
        os.environ[ENV_VAR] = previous


def test_handler_class():
    logger = get_logger("test_base", handler_class=FakeHandler)
    assert len(logger.handlers) == 1
    handler = logger.handlers[0]
    assert isinstance(handler, FakeHandler)


def test_base():
    logger = get_logger("test_base", handler_class=FakeHandler)
    assert logger.level == DEFAULT_LEVEL == logging.INFO
    logger.debug("base_test_debug")
    logger.info("base_test_info")
    logger.warning("base_test_warning")

    handler = logger.handlers[0]
    assert isinstance(handler, FakeHandler)
    assert len(handler.msgs) == 2
    assert "base_test_info" in handler.msgs[0]
    assert "base_test_warning" in handler.msgs[1]


@pytest.mark.parametrize("params", [
    # Examples from the README
    dict(debug=True),
    dict(level="DEBUG"),
    dict(level=logging.DEBUG),
])
def test_debug(params):
    logger = get_logger("test_debug", handler_class=FakeHandler, **params)
    assert logger.level == logging.DEBUG


def test_debug_env(env_debug):
    logger = get_logger("test_debug_env", handler_class=FakeHandler)
    assert logger.level == logging.DEBUG


def test_two_handlers():
    logger1 = get_logger("test_two_handlers", handler_class=FakeHandler)
    logger2 = get_logger("test_two_handlers", handler_class=FakeHandler)
    assert logger1 == logger2
    assert len(logger1.handlers) == 2


def test_level():
    logger = get_logger("test_level", level=logging.ERROR, handler_class=FakeHandler)
    assert logger.level == logging.ERROR
