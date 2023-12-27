"""Module that defines a base of the handlers and all the library handlers.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.StdoutHandler

    As example.
"""

import datetime
import sys

from os import PathLike

from .formatters import Formatter, PlainFormatter
from .logging_context import LoggingContext
from .defaults import DEFAULT_LOGGING_CONTEXT
from ._types import LogLevel

from abc import abstractmethod
from typing import TextIO, Any

__all__ = ['Handler', 'IOHandler', 'StdoutHandler', 'StderrHandler', 'FileHandler']


class Handler:
    """A base of all the handlers.

    :ivar log_level: Log level.
    :type log_level: LogLevel
    :ivar formatter: Formatter that will use this handler.
    :type formatter: Formatter
    :ivar logging_context: Logging context.
    :type logging_context: LoggingContext
    :ivar log_exceptions: Determines whether log exceptions or not.
    :type log_exceptions: bool
    :ivar enabled: Determines whether log any message or not. Isn't recommended to change it manually, but you may. Is
        recommended to use :meth:`enable()` and :meth:`disable()` methods.
    :type enabled: bool
    """

    def __init__(self,
                 log_level: LogLevel = 'info',
                 formatter: Formatter = PlainFormatter(),
                 logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT,
                 log_exceptions: bool = True,
                 enabled: bool = True,
                 ):
        """
        :param log_level: Log level.
        :type log_level: LogLevel
        :param formatter: Formatter that will use this handler.
        :type formatter: Formatter
        :param logging_context: Logging context.
        :type logging_context: LoggingContext
        :param log_exceptions: Determines whether log exceptions or not.
        :type log_exceptions: bool
        :param enabled: Determines whether log any message or not.
        :type enabled: bool
        """
        self.log_level        = log_level
        self.formatter        = formatter
        self.logging_context  = logging_context
        self.log_exceptions   = log_exceptions
        self.enabled          = enabled

    def enable(self):
        """Enables handler."""

        self.enabled = True

    def disable(self):
        """Disables handler."""

        self.enabled = False

    @abstractmethod
    def write(self,
              message: str,
              level: str | int,
              logger_color: str,
              logger_name: str,
              group_name: str,
              group_color: str,
              exc: Exception | None = None,
              time: datetime.datetime | None = None,
              fmt_args: list[Any] | None = None,
              fmt_kwargs: dict[str, Any] | None = None):
        raise NotImplementedError('Method "write()" isn\'t implemented!')


class IOHandler(Handler):
    """A base of IO handlers.

    :ivar io: IO to be used to write messages.
    :type io: TextIO
    """

    def __init__(self, io: TextIO, *args: Any, **kwargs: dict[str, Any]):
        """
        :param io: IO to be used to write messages.
        :type io: TextIO
        """
        super().__init__(*args, **kwargs)

        self.io = io

    def write(self,
              message: str,
              level: str | int,
              logger_color: str,
              logger_name: str,
              group_name: str,
              group_color: str,
              exc: Exception | None = None,
              time: datetime.datetime | None = None,
              fmt_args: list[Any] | None = None,
              fmt_kwargs: dict[str, Any] | None = None):
        if not self.enabled:
            return

        if self.logging_context.log_level(self.log_level, level):

            # log formatted message
            self.io.write(self.formatter.format(
                message,
                time,
                level,
                logger_color,
                logger_name,
                group_name,
                group_color,
                fmt_args, fmt_kwargs)+'\n')

            # format and write exception to io if exceptions logging is enabled and exception was given
            if self.log_exceptions and exc is not None:
                self.io.write(self.formatter.format_exception(exc)+'\n')

            self.io.flush()

    def set_level(self, level: LogLevel):
        """Sets log level of handler to given.

        :param level: Log level.
        :type level: LogLevel
        """
        self.log_level = level


class StdoutHandler(IOHandler):
    """Handles stdout output (console).
    This class is shorthand for IOHandler(sys.stdout, ...)."""

    def __init__(self, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(sys.stdout, *args, **kwargs)


class StderrHandler(IOHandler):
    """Handles stderr output (console).
    This class is shorthand for IOHandler(sys.stdout, ...)."""

    def __init__(self, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(sys.stderr, *args, **kwargs)


class FileHandler(IOHandler):
    """Handles file output.

    :ivar file_io: Opened file object.
    :type file_io: TextIO
    :ivar path: Path to the file.
    :type path: str | bytes | PathLike[str] | PathLike[bytes] | int
    :ivar encoding: Encoding, by default is the UTF-8.
    :type encoding: str"""

    def __init__(self,
                 path: str | bytes | PathLike[str] | PathLike[bytes] | int,
                 encoding: str = 'utf8',
                 *args: Any,
                 **kwargs: dict[str, Any]
                 ):
        """
        :param path: Path to the file.
        :type path: str | bytes | PathLike[str] | PathLike[bytes] | int
        :param encoding: Encoding, by default is the UTF-8.
        :type encoding: str
        """
        self.file_io   = open(path, 'w', encoding=encoding)
        self.path      = path
        self.encoding  = encoding

        super().__init__(self.file_io, *args, **kwargs)

    def __del__(self):
        self.file_io.close()
