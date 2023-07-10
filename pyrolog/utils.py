
import inspect

from .logging_context import LoggingContext
from .defaults import DEFAULT_LOGGING_CONTEXT
from .formatters import PlainFormatter, defined_formatters

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .logger import Logger


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
