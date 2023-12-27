"""Module with the default definitions of library.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.defaults.DEFAULT_LOG_LEVELS

    As example.
"""

from .logging_context import LoggingContext
from .colors import *

DEFAULT_LOG_LEVELS = {
    'debug': 5,
    'exception': 10,
    'info': 15,
    'warn': 20,
    'error': 25,
    'critical': 30,
    'notset': 9999,
}
"""The default log levels dictionary."""

MINIMAL_FORMAT_STRING = '{level:<{level_offset}} {message}'
"""The minimal formatter specification, which is the default and recommended for small projects."""

TIMED_MINIMAL_FORMAT_STRING = '{time} {level:<{level_offset}} {message}'
"""The minimal formatter specification, but with specified time."""

MINIMAL_TIME_FORMAT_STRING = '{hour:02d}:{minute:02d}:{second:02d}.{microsecond}'
"""The default minimal time format specification."""

MAXIMUM_TIME_FORMAT_STRING = '{year:04d}.{month:02d}.{day:02d} {hour:02d}:{minute:02d}:{second:02d}.{microsecond}'
"""Time Format specification that is recommended for professional, large projects."""

MAXIMUM_TIME_FORMAT_STRING_FILENAME_SAFE = '{year:04d}_{month:02d}_{day:02d}-{hour:02d}_{minute:02d}_{second:02d}_{microsecond}'
"""Time Format specification that is recommended for filename of the log files."""

MAXIMUM_FORMAT_STRING = '{time} | {level:<{level_offset}} | {group_name:<{group_name_offset}} | {logger_name:<{logger_name_offset}} -> {message}'
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

COLORED_MAXIMUM_TIME_FORMAT_STRING = '{fore.cyan}{year:04d}{fore.reset}.{fore.cyan}{month:02d}{fore.reset}.{fore.cyan}{day:02d}{fore.reset} {fore.cyan}{hour:02d}{fore.reset}:{fore.cyan}{minute:02d}{fore.reset}:{fore.cyan}{second:02d}{fore.reset}.{fore.lightmagenta}{microsecond}{fore.reset}'
"""Colored time format specification that is recommended for professional, large projects."""

COLORED_MAXIMUM_FORMAT_STRING = '{time} | {level_color}{level:<{level_offset}}{reset} | {group_color}{group_name:<{group_name_offset}}{reset} | {logger_color}{logger_name:<{logger_name_offset}}{reset} -> {message}'
"""Colored format specification that is recommended for professional, large projects."""
