import os
import logging
from libs.test_context import TestContext

class Logger:
    TestContext.init()

    _logger = None
    _log_handler = None
    _log_dir = TestContext.log_dir
    rp_logger = None

    @classmethod
    def init(cls, logger_name=__name__):
        cls._logger = logging.getLogger(logger_name)
        cls._logger.setLevel(logging.DEBUG)

    @classmethod
    def add_log_handler(cls, log_file, **kwargs):
        if cls._logger is not None:
            log_dir = os.path.join(Logger._log_dir, kwargs.get('log_dir', ''))

            if (not os.path.exists(log_dir)):
                os.makedirs(log_dir)

            log_file = os.path.join(log_dir, log_file)
            cls._log_handler = logging.FileHandler(filename=log_file)
            cls._log_handler.setFormatter(logging.Formatter(fmt='%(asctime)s|%(levelname)s|%(message)s'))
            cls._logger.addHandler(cls._log_handler)

    @classmethod
    def remove_log_handler(cls):
        if (cls._logger is not None) and (cls._log_handler is not None):
            cls._logger.removeHandler(cls._log_handler)
            cls._log_handler.close()
            cls._log_handler = None

    @classmethod
    def info(cls, msg):
        if cls._logger is not None:
            cls._logger.info(msg)
        return msg

    @classmethod
    def warning(cls, msg):
        if cls._logger is not None:
            cls._logger.warn(msg)
        return msg

    @classmethod
    def error(cls, msg):
        if cls._logger is not None:
            cls._logger.error(msg)
        return msg

    @classmethod
    def disabled(cls, disabled=True):
        if cls._logger is not None:
            cls._logger.disabled = disabled
