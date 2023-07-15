
"""
    Pyrolog. Pretty logging library.
    Copyright (C) 2023  ftdot (https://github.com/ftdot)
"""

from . import defaults
from . import _types as types
from . import utils
from . import empty_colors

from ._types import LogOnlyLevels

from .group import *
from .logger import *
from .logging_context import *
from .handlers import *
from .formatters import *
from .version import *
from .colors import *


def get_plain_logger(log_level: types.LogLevel = 'info'):
    """Gets logger (unnamed) with StdoutHandler and plain formatter. Also, uses given log level.

    :param log_level: Log level
    :type log_level: types.LogLevel
    """

    return Logger(
        handlers=[StdoutHandler(log_level=log_level), ]
    )


def get_colored_logger(log_level: types.LogLevel = 'info'):
    """Gets logger (unnamed) with StdoutHandler and colored formatter. Also, uses given log level.

    :param log_level: Log level
    :type log_level: types.LogLevel
    """

    return Logger(
        handlers=[StdoutHandler(log_level=log_level, formatter=ColoredFormatter()), ]
    )
