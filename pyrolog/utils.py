"""This module contains utilities of the library.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.utils.make_new_log_level(...)

    As example.
"""

import inspect

from datetime import datetime

from .logging_context import LoggingContext
from .defaults import DEFAULT_LOGGING_CONTEXT, MAXIMUM_TIME_FORMAT_STRING_FILENAME_SAFE
from .formatters import PlainFormatter, defined_formatters

from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from .logger import Logger


__all__ = ['make_logger_binding', 'make_new_log_level', 'update_logger_name_offset',
           'update_group_name_offset', 'get_filename_timestamp']


def make_logger_binding(level: str) -> Callable:
    """Makes function-bind for given level.

    :param level: Level.
    :type level: str

    :returns: Function-bind for given level.
    :rtype: Callable
    """

    def f(self: 'Logger', message: str, *args, exc: Exception | None = None, **kwargs):
        self.record(message, level, *args, exc=exc, stack=inspect.stack()[1], **kwargs)

    return f


def make_new_log_level(logger_class: 'Logger',
                       name: str,
                       level: int,
                       logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT
                       ):
    """Makes new log level and function-bind for it. Also adds function-bind to :class:`Logger` class.
    **Note** that `name` will be converted to **lower case**!

    :param logger_class: Class of the logger.
    :type logger_class: Logger
    :param name: Name of the new log level.
    :type name: str
    :param level: Int level of the new log level.
    :type level: int
    :param logging_context: Logging context where it will be registered.
    :type logging_context: LoggingContext
    """

    name = name.lower()
    logging_context.log_levels[name] = level

    # make function-bind for the log level
    setattr(logger_class, name, make_logger_binding(name))

    # update level offset
    for f in defined_formatters:
        if hasattr(f, 'offsets') and f.offsets and f.logging_context is logging_context:
            f.static_variables['level_offset'] = logging_context.get_level_offset()


def update_logger_name_offset(logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT):
    """Updates logger name offset.

    :param logging_context: Current logging context.
    :type logging_context: LoggingContext
    """

    for f in defined_formatters:
        if hasattr(f, 'offsets') and f.offsets and f.logging_context is logging_context:
            f.static_variables['logger_name_offset'] = logging_context.get_logger_name_offset()


def update_group_name_offset(logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT):
    """Updates group name offset.

    :param logging_context: Current logging context.
    :type logging_context: LoggingContext
    """

    for f in defined_formatters:
        if hasattr(f, 'offsets') and f.offsets and f.logging_context is logging_context:
            f.static_variables['group_name_offset'] = logging_context.get_group_name_offset()


def get_filename_timestamp(format_string=MAXIMUM_TIME_FORMAT_STRING_FILENAME_SAFE + '.log'):
    """Makes pretty filename with time and ".log" extension.

    :param format_string: Format string.
    :type format_string: str
    """

    return PlainFormatter(time_format_string=format_string).format_time(datetime.now())
