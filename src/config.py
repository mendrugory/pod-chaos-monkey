import logging
import sys
import os

_DEFAULT_FORMAT='[%(name)s]: %(message)s'
_LOGGER_NAME='pod-chaos-monkey'
_LOGGER_LEVEL_NAME="LOGGER_LEVEL"
_DEFAULT_LOGGER_LEVEL=logging._levelToName[logging.INFO]
ENV_KUBERNETES="KUBERNETES"
_ENVIRONMENT_NAME="ENVIRONMENT"
_DEFAULT_ENVIRONMENT=ENV_KUBERNETES


_logger = None
_logger_level=None
_environment=None

def get_environment():
    global _environment
    if _environment is None:
        _environment=os.getenv(_ENVIRONMENT_NAME, _DEFAULT_ENVIRONMENT)
    return _environment

def get_logger_level():
    global _logger_level
    if _logger_level is None:
        _logger_level = logging._nameToLevel[os.getenv(_LOGGER_LEVEL_NAME, _DEFAULT_LOGGER_LEVEL)]
    return _logger_level

def get_logger():
    global _logger
    if _logger is None:
        _logger = _get_custom_logger(_LOGGER_NAME, level=get_logger_level())
    return _logger

def _get_custom_logger(logger_name, format=_DEFAULT_FORMAT, level=logging.INFO):
    logger_format = logging.Formatter(format)
    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setFormatter(logger_format)
    logger_handler.setLevel(level)
    logger = logging.getLogger(logger_name)
    logger.addHandler(logger_handler)
    logger.setLevel(level)
    return logger
