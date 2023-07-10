
from functools import lru_cache

from typing import Any, TypeAlias, Literal

ColorDict: TypeAlias     = dict[Literal['types'] | Literal['levels'], dict[str | type, Any]]
VarDict: TypeAlias       = dict[str, Any]
LogLevelDict: TypeAlias  = dict[str, int]


class LogOnlyLevels:

    def __init__(self, levels: str | list[str]):
        """Determines which level(s) will be logged and which not.

        Example usage:

        .. code-block:: python

            import pyrolog
            stdout_handler = pyrolog.StdoutHandler(
                log_level=pyrolog.LogOnlyLevels(
                    ['debug', 'info', 'warn']
                ),
                formatter=pyrolog.PlainFormatter()
            )
            stderr_handler = pyrolog.StderrHandler(
                log_level=pyrolog.LogOnlyLevels(
                    ['exception', 'error', 'critical']
                ),
                formatter=pyrolog.PlainFormatter()
            )

        When using this handler, only the specified levels will be logged.

        :param levels: Level(s) to be logged only
        :type levels: str | list[str]
        """

        self.levels = [levels, ] if isinstance(levels, str) else levels

    @lru_cache(10)
    def log_level(self, level: str):
        return level in self.levels

LogLevel: TypeAlias = str | int | LogOnlyLevels
