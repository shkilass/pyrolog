
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

    def __init__(self,
                 log_level: LogLevel = 'info',
                 formatter: Formatter = PlainFormatter(),
                 logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT,
                 log_exceptions: bool = True,
                 enabled: bool = True,
                 ):
        self.log_level        = log_level
        self.formatter        = formatter
        self.logging_context  = logging_context
        self.log_exceptions   = log_exceptions
        self.enabled          = enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    @abstractmethod
    def write(self,
              message: str,
              level: str | int,
              logger_color: str,
              logger_name: str,
              exc: Exception | None = None,
              time: datetime.datetime | None = None,
              fmt_args: list[Any] | None = None,
              fmt_kwargs: dict[str, Any] | None = None):
        raise NotImplementedError('Method "write()" isn\'t implemented!')


class IOHandler(Handler):

    def __init__(self, io: TextIO, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(*args, **kwargs)

        self.io = io

    def write(self,
              message: str,
              level: str | int,
              logger_color: str,
              logger_name: str,
              exc: Exception | None = None,
              time: datetime.datetime | None = None,
              fmt_args: list[Any] | None = None,
              fmt_kwargs: dict[str, Any] | None = None):
        if not self.enabled:
            return

        if self.logging_context.log_level(self.log_level, level):

            # log formatted message
            self.io.write(self.formatter.format(message, time, level, logger_color, logger_name, fmt_args, fmt_kwargs)+'\n')

            # format and write exception to io if exceptions logging is enabled and exception was given
            if self.log_exceptions and exc is not None:
                self.io.write(self.formatter.format_exception(exc)+'\n')

            self.io.flush()


class StdoutHandler(IOHandler):

    def __init__(self, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(sys.stdout, *args, **kwargs)


class StderrHandler(IOHandler):

    def __init__(self, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(sys.stderr, *args, **kwargs)


class FileHandler(IOHandler):

    def __init__(self, path: str | bytes | PathLike[str] | PathLike[bytes] | int, *args: Any, **kwargs: dict[str, Any]):
        self.file_io  = open(path, 'w')
        self.path     = path

        super().__init__(self.file_io, *args, **kwargs)

    def __del__(self):
        self.file_io.close()
