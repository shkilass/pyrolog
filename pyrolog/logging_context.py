"""Dedicated module for the :class:`LoggingContext` class.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.LoggingContext

    As example.
"""

from functools import lru_cache

from ._types import LogLevelDict, LogOnlyLevels, LogLevel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .logger import Logger
    from .group import Group

__all__ = ['LoggingContext']


class LoggingContext:
    """Defines some variables that is "unique" for every logging context.

    :ivar log_levels: Dict with the registered log levels.
    :type log_levels: LogLevelDict
    :ivar loggers: List with the loggers pinned to logging context instance.
    :type loggers: list[Logger]
    :ivar groups: List with the groups pinned to logging context instance.
    :type groups: list[Group]
    :ivar groups_by_name: Dictionary with groups with names as keys.
    :type groups_by_name: dict[str, 'Group']
    """

    def __init__(self, log_levels: LogLevelDict):
        """
        :param log_levels: Dict with the registered log levels.
        :type log_levels: LogLevelDict
        """

        self.log_levels = log_levels

        self.loggers: list['Logger']             = []
        self.groups: list['Group']               = []
        self.groups_by_name: dict[str, 'Group']  = {}

    def enable_all_loggers(self):
        """Enables all loggers pinned to the logging context."""

        for l in self.loggers:
            l.enable()

    def disable_all_loggers(self):
        """Disables all loggers pinned to the logging context."""

        for l in self.loggers:
            l.disable()

    def enable_all_groups(self):
        """Enables all groups pinned to the logging context."""

        for g in self.groups:
            g.enable()

    def disable_all_groups(self):
        """Disables all groups pinned to the logging context."""

        for g in self.groups:
            g.disable()

    def get_level_offset(self):
        return len(max(self.log_levels, key=len))

    def get_logger_name_offset(self):
        return 0 if len(self.loggers) == 0 else len(max(self.loggers, key=lambda g: len(g.name)).name)

    def get_group_name_offset(self):
        return 0 if len(self.groups) == 0 else len(max(self.groups, key=lambda g: len(g.name_path)).name_path)

    @lru_cache(10)
    def log_level(self, level: LogLevel, context_level: str | int):

        if isinstance(level, LogOnlyLevels):
            if isinstance(context_level, int):
                context_level = self.log_levels.keys()[self.log_levels.values().index(context_level)]

            return level.log_level(context_level)

        elif isinstance(level, str):
            if isinstance(context_level, str):
                context_level = self.log_levels[context_level]

            return self.log_levels[level] <= context_level
        elif isinstance(level, int):
            if isinstance(context_level, str):
                context_level = self.log_levels[context_level]

            return level <= context_level
