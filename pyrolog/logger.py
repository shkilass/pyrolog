
from datetime import datetime

from .handlers import Handler
from .utils import make_logger_binding, update_logger_name_offset
from .logging_context import LoggingContext
from .defaults import DEFAULT_LOGGING_CONTEXT
from .colors import TextColor, BGColor, TextStyle

from typing import Any, Self

__all__ = ['Logger']


class Logger:
    """A logger object.

    :ivar name: Name of the logger
    :type name: str
    :ivar handlers: Handlers to be used by logger
    :type handlers: Handler | list[Handler] | None
    :ivar logging_context: The current logging context (by default is defaults.DEFAULT_LOGGING_CONTEXT)
    :type logging_context: LoggingContext
    """

    def __init__(self,
                 name: str = '',
                 handlers: Handler | list[Handler] | None = None,
                 logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT,
                 logger_color: TextColor | BGColor | TextStyle | str = '',
                 ):
        """Creates a new Logger object.

        :param name: Name of the logger (by default it is empty)
        :type name: str | None
        :param handlers: Handlers to be used by logger
        :type handlers: Handler | list[Handler] | None
        :param logging_context: The current logging context (by default is defaults.DEFAULT_LOGGING_CONTEXT)
        :type logging_context: LoggingContext
        """

        self.name             = name
        self.handlers         = [handlers, ] if isinstance(handlers, Handler) else handlers
        self.logging_context  = logging_context
        self.logger_color     = logger_color

        logging_context.loggers.append(self)
        update_logger_name_offset(logging_context)

    def record(self,
               message: str,
               level: str | int,
               *args: Any,
               exc: Exception | None = None,
               **kwargs: dict[str, Any]):
        """Records a message at the specified logging level.

        :param message: Message to be logged
        :type message: str
        :param level: Logged level
        :type level:
        :param args: Positioned arguments for formatting
        :type args: Any
        :param exc: Exception to pin with log message
        :type exc: Exception
        :param kwargs: Named arguments for formatting
        :type kwargs: dict[str, Any]
        """

        for h in self.handlers:
            h.write(
                message,
                level,
                self.logger_color,
                self.name,
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
        """Logs debug message. Shorthand for :method:`Logger.record()` with `level='debug'`

        :param message: Message to be logged
        :type message: str
        :param args: Positioned arguments for formatting
        :type args: Any
        :param exc: Exception to pin with log message
        :type exc: Exception
        :param kwargs: Named arguments for formatting
        :type kwargs: dict[str, Any]
        """
        ...

    def exception(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs exception message. Shorthand for :method:`Logger.record()` with `level='exception'`

        :param message: Message to be logged
        :type message: str
        :param args: Positioned arguments for formatting
        :type args: Any
        :param exc: Exception to pin with log message
        :type exc: Exception
        :param kwargs: Named arguments for formatting
        :type kwargs: dict[str, Any]
        """
        ...

    def info(self, message: str, *args: Any, exception: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs info message. Shorthand for :method:`Logger.record()` with `level='info'`

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
        """Logs warn message. Shorthand for :method:`Logger.record()` with `level='info'`

        :param message: Message to be logged
        :type message: str
        :param args: Positioned arguments for formatting
        :type args: Any
        :param exc: Exception to pin with log message
        :type exc: Exception
        :param kwargs: Named arguments for formatting
        :type kwargs: dict[str, Any]
        """
        ...

    def error(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs error message. Shorthand for :method:`Logger.record()` with `level='info'`

        :param message: Message to be logged
        :type message: str
        :param args: Positioned arguments for formatting
        :type args: Any
        :param exc: Exception to pin with log message
        :type exc: Exception
        :param kwargs: Named arguments for formatting
        :type kwargs: dict[str, Any]
        """
        ...

    def critical(self, message: str, *args: Any, exc: Exception | None = None, **kwargs: dict[str, Any]):
        """Logs critical message. Shorthand for :method:`Logger.record()` with `level='info'`

        :param message: Message to be logged
        :type message: str
        :param args: Positioned arguments for formatting
        :type args: Any
        :param exc: Exception to pin with log message
        :type exc: Exception
        :param kwargs: Named arguments for formatting
        :type kwargs: dict[str, Any]
        """
        ...

Logger.bind_log_methods()
