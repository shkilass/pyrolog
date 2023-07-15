"""Dedicated module for the :class:`Logger` class.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.Logger

    As example.
"""

from datetime import datetime

from .handlers import Handler
from .utils import make_logger_binding, update_logger_name_offset
from .logging_context import LoggingContext
from .defaults import DEFAULT_LOGGING_CONTEXT

from typing import TYPE_CHECKING, Any, Self

if TYPE_CHECKING:
    from .group import Group

__all__ = ['Logger']


class Logger:
    """A logger object.

    :ivar name: Name of the logger.
    :type name: str
    :ivar handlers: Handlers to be used by logger.
    :type handlers: list[Handler]
    :ivar logging_context: The current logging context. (by default is defaults.DEFAULT_LOGGING_CONTEXT)
    :type logging_context: LoggingContext
    """

    def __init__(self,
                 name: str = '',
                 handlers: Handler | list[Handler] | None = None,
                 logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT,
                 logger_color: str = '',
                 group: 'Group | str | None' = None,
                 enabled: bool = True,
                 ):
        """Creates a new Logger object.

        :param name: Name of the logger. (by default it is empty)
        :type name: str | None
        :param handlers: Handlers to be used by logger.
        :type handlers: Handler | list[Handler] | None
        :param logging_context: The current logging context. (by default is defaults.DEFAULT_LOGGING_CONTEXT)
        :type logging_context: LoggingContext
        :param logger_color: Color of the logger. (visible only by using ColoredFormatter)
        :type logger_color: str
        :param group: Group of the logger. If it is not None, then copies all parameters from that group.
        :type group: Group | None
        :param enabled: If it is set to False, logger will not log any messages.
        :type enabled: bool
        """

        if group is not None:
            self.handlers         = group.handlers
            self.logging_context  = group.logging_context
            self.enabled          = group.enabled

            self.group_name_path = group.name_path
            self.group_color = group.group_color

            group.loggers.append(self)

        else:
            self.handlers         = [handlers, ] if isinstance(handlers, Handler) else handlers
            self.logging_context  = logging_context
            self.enabled          = enabled

            self.group_name_path = '*'
            self.group_color = ''

        self.name          = name
        self.logger_color  = logger_color
        self.group         = group

        self.logging_context.loggers.append(self)
        update_logger_name_offset(self.logging_context)

    def enable(self):
        """Enables a logger."""
        self.enabled = True

    def disable(self):
        """Disables a logger."""
        self.enabled = False

    def record(self,
               message: str,
               level: str | int,
               *args: Any,
               exc: Exception | None = None,
               **kwargs: dict[str, Any]):
        """Records a message at the specified logging level.

        :param message: Message to be logged.
        :type message: str
        :param level: Logged level.
        :type level:
        :param args: Positioned arguments for formatting.
        :type args: Any
        :param exc: Exception to pin with log message.
        :type exc: Exception
        :param kwargs: Named arguments for formatting.
        :type kwargs: dict[str, Any]
        """

        if not self.enabled:
            return

        for h in self.handlers:
            h.write(
                message,
                level,
                self.logger_color,
                self.name,
                self.group_name_path,
                self.group_color,
                exc=exc,
                time=datetime.now(),
                fmt_args=args,
                fmt_kwargs=kwargs,
            )

    @staticmethod
    def bind_log_methods():
        """Binds all log methods for the Logger object instance."""

        for level in DEFAULT_LOGGING_CONTEXT.log_levels:
            setattr(Logger, level, make_logger_binding(level))

    ####

    # These methods are implemented by "_bind_log_methods()" method (when the Logger object initialized)

    def debug(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs debug message. Shorthand for :method:`Logger.record()` with `level='debug'`.

        :param message: Message to be logged.
        :type message: str
        :param args: Positioned arguments for formatting.
        :type args: Any
        :param exc: Exception to pin with log message.
        :type exc: Exception
        :param kwargs: Named arguments for formatting.
        :type kwargs: dict[str, Any]
        """
        ...

    def exception(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs exception message. Shorthand for :method:`Logger.record()` with `level='exception'`.

        :param message: Message to be logged.
        :type message: str
        :param args: Positioned arguments for formatting.
        :type args: Any
        :param exc: Exception to pin with log message.
        :type exc: Exception
        :param kwargs: Named arguments for formatting.
        :type kwargs: dict[str, Any]
        """
        ...

    def info(self, message: str, *args: Any, exception: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs info message. Shorthand for :method:`Logger.record()` with `level='info'`.

        :param message: Message to be logged
        :type message: str
        :param args: Positioned arguments for formatting
        :type args: Any
        :param exception: Exception to pin with log message
        :type exception: Exception
        :param kwargs: Named arguments for formatting
        :type kwargs: dict[str, Any]
        """
        ...

    def warn(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs warn message. Shorthand for :method:`Logger.record()` with `level='info'`.

        :param message: Message to be logged.
        :type message: str
        :param args: Positioned arguments for formatting.
        :type args: Any
        :param exc: Exception to pin with log message.
        :type exc: Exception
        :param kwargs: Named arguments for formatting.
        :type kwargs: dict[str, Any]
        """
        ...

    def error(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs error message. Shorthand for :method:`Logger.record()` with `level='info'`.

        :param message: Message to be logged.
        :type message: str
        :param args: Positioned arguments for formatting.
        :type args: Any
        :param exc: Exception to pin with log message.
        :type exc: Exception
        :param kwargs: Named arguments for formatting.
        :type kwargs: dict[str, Any]
        """
        ...

    def critical(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs critical message. Shorthand for :method:`Logger.record()` with `level='info'`.

        :param message: Message to be logged.
        :type message: str
        :param args: Positioned arguments for formatting.
        :type args: Any
        :param exc: Exception to pin with log message.
        :type exc: Exception
        :param kwargs: Named arguments for formatting.
        :type kwargs: dict[str, Any]
        """
        ...

Logger.bind_log_methods()
