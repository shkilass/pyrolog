
from .logging_context import LoggingContext
from .colors import *

DEFAULT_LOG_LEVELS = {
    'debug': 5,
    'exception': 10,
    'info': 15,
    'warn': 20,
    'error': 25,
    'critical': 30
}
"""The default log levels dictionary."""

MINIMAL_FORMAT_STRING = '{level:<{level_offset}} {message}'
"""The minimal formatter specification, which is the default and recommended for small projects."""

TIMED_MINIMAL_FORMAT_STRING = '{time} {level:<{level_offset}} {message}'
"""The minimal formatter specification, but with specified time."""

MINIMAL_TIME_FORMAT_STRING = '{hour:02d}:{minute:02d}:{second:02d}.{microsecond}'
"""The default minimal time format specification."""

MAXIMUM_FORMAT_STRING = '{time} | {level:<{level_offset}} | {logger_name:<{logger_name_offset}} -> {message}'
"""Format specification that is recommended for professional, large projects."""

DEFAULT_LOGGING_CONTEXT = LoggingContext(DEFAULT_LOG_LEVELS)
"""The logging context that is used by all elements of the logging library by default."""

DEFAULT_COLOR_DICT = {
    'types': {
        int: TextColor.lightmagenta,
        float: TextColor.lightmagenta + TextStyle.bold,
        bool: TextColor.yellow,
        str: TextColor.lightgreen,
        bytes: TextColor.lightred + TextStyle.bold,
        list: TextColor.lightyellow,
        tuple: TextColor.lightyellow + TextStyle.bold,
        dict: TextColor.cyan,
        'exception': TextColor.lightred,
        'all': TextColor.lightcyan + TextStyle.bold,
    },
    'levels': {
        'debug': TextColor.lightwhite,
        'exception': TextColor.lightyellow,
        'info': TextColor.lightcyan,
        'warn': TextColor.yellow,
        'error': TextColor.lightred,
        'critical': TextColor.red + TextStyle.bold,
    }
}
"""The default color dict that is used by ColoredFormatter"""

COLORED_MINIMAL_FORMAT_STRING = '{level_color}{level:<{level_offset}}{reset} {message}'
"""The colored minimal formatter specification, which is the default for the colored formatter and recommended for small projects."""

COLORED_TIMED_MINIMAL_FORMAT_STRING = '{time} {level_color}{level:<{level_offset}}{reset} {message}'
"""The minimal colored formatter specification, but with specified time."""

COLORED_MINIMAL_TIME_FORMAT_STRING = '{fore.cyan}{hour:02d}{fore.reset}:{fore.cyan}{minute:02d}{fore.reset}:{fore.cyan}{second:02d}{fore.reset}.{fore.lightmagenta}{microsecond}{fore.reset}'
"""The default colored minimal time format specification."""

COLORED_MAXIMUM_FORMAT_STRING = '{time} | {level_color}{level:<{level_offset}}{reset} | {logger_color}{logger_name:<{logger_name_offset}}{reset} -> {message}'
"""Colored format specification that is recommended for professional, large projects."""
