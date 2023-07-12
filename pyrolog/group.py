
from .handlers import Handler
from .logging_context import LoggingContext
from .logger import Logger
from .colors import TextColor, BGColor, TextStyle
from .defaults import DEFAULT_LOGGING_CONTEXT
from .utils import update_group_name_offset

__all__ = ['Group']


class Group:

    def __init__(self,
                 name: str = '',
                 handlers: Handler | list[Handler] | None = None,
                 logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT,
                 group_color: TextColor | BGColor | TextStyle | str = '',
                 enabled: bool = True,
                 parent_group: 'Group | None' = None
                 ):

        if parent_group is None:
            if handlers is None:
                self.handlers = []
            else:
                self.handlers         = [handlers, ] if isinstance(handlers, Handler) else handlers

            self.logging_context  = logging_context
            self.group_color      = group_color
            self.enabled          = enabled
            self.name_path        = name

        else:
            self.handlers         = parent_group.handlers
            self.logging_context  = parent_group.logging_context
            self.enabled          = parent_group.enabled
            self.name_path        = parent_group.name_path + '.' + name

            parent_group.subgroups.append(self)

        self.group_color              = group_color
        self.name                     = name
        self.subgroups: list[Group]   = []
        self.loggers: list['Logger']  = []
        self.parent_group             = parent_group

        self.logging_context.groups.append(self)
        update_group_name_offset(self.logging_context)

    def enable(self):
        self.enabled = True

        for l in self.loggers:
            l.enable()

        for sg in self.subgroups:
            sg.enable()

    def disable(self):
        self.enabled = False

        for l in self.loggers:
            l.disable()

        for sg in self.subgroups:
            sg.disable()

    def subgroup(self, *args, **kwargs):
        return Group(*args, **kwargs, parent_group=self)

    def logger(self, *args, **kwargs):
        return Logger(*args, **kwargs, group=self)
