
import inspect

from datetime import datetime

from .logging_context import LoggingContext
from .defaults import DEFAULT_LOGGING_CONTEXT, MAXIMUM_TIME_FORMAT_STRING_FILENAME_SAFE
from .formatters import PlainFormatter, defined_formatters

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .logger import Logger


__all__ = ['make_logger_binding', 'make_new_log_level', 'update_logger_name_offset',
           'update_group_name_offset', 'get_filename_timestamp']


def make_logger_binding(level: int):
    def f(self: 'Logger', message: str, *args, exc: Exception | None = None, **kwargs):
        self.record(message, level, *args, exc=exc, stack=inspect.stack()[1], **kwargs)

    return f


def make_new_log_level(logger_class: 'Logger',
                       name: str,
                       level: int,
                       logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT
                       ):
    name = name.lower()
    logging_context.log_levels[name] = level

    setattr(logger_class, name, make_logger_binding(name))

    for f in defined_formatters:
        if hasattr(f, 'offsets') and f.offsets and f.logging_context is logging_context:
            f.static_variables['level_offset'] = logging_context.get_level_offset()


def update_logger_name_offset(logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT):
    for f in defined_formatters:
        if hasattr(f, 'offsets') and f.offsets and f.logging_context is logging_context:
            f.static_variables['logger_name_offset'] = logging_context.get_logger_name_offset()


def update_group_name_offset(logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT):
    for f in defined_formatters:
        if hasattr(f, 'offsets') and f.offsets and f.logging_context is logging_context:
            f.static_variables['group_name_offset'] = logging_context.get_group_name_offset()


def get_filename_timestamp(format_string=MAXIMUM_TIME_FORMAT_STRING_FILENAME_SAFE + '.log'):
    return PlainFormatter(time_format_string=format_string).format_time(datetime.now())
