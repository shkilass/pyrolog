"""Dedicated module for :class:`Group` class.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.Group

    As example.
"""

from .handlers import Handler
from .logging_context import LoggingContext
from .logger import Logger
from .defaults import DEFAULT_LOGGING_CONTEXT
from .utils import update_group_name_offset

__all__ = ['Group']


class Group:
    """A group class, that very helpful if you use many loggers in your project.

    :ivar name: Name of the group.
    :type name: str
    :ivar handlers: Handlers to be used by loggers.
    :type handlers: list[Handler]
    :ivar logging_context: The current logging context. (by default is `defaults.DEFAULT_LOGGING_CONTEXT` of
        :mod:`pyrolog.defaults` module)
    :type logging_context: LoggingContext
    :ivar group_color: Color of the group. (visible only by using ColoredFormatter)
    :type group_color: str
    :ivar enabled: If it is set to False, all pinned loggers will not log any messages and all subgroups pinned to
        will be disabled. Do not change it manually, use :meth:`Group.disable()` and :meth:`Group.enable()`.
    :type enabled: bool
    :ivar parent_group: Parent group of this group.
    :type parent_group: Group | None
    :ivar subgroups: Subgroups of this group.
    :type subgroups: list[Group]
    :ivar loggers: Loggers pinned to this group.
    :type loggers: list[Logger]
    """

    def __init__(self,
                 name: str = '',
                 handlers: Handler | list[Handler] | None = None,
                 logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT,
                 group_color: str = '',
                 enabled: bool = True,
                 parent_group: 'Group | str | None' = None
                 ):
        """
        :param name: Name of the group.
        :type name: str
        :param handlers: Handlers to be used by loggers.
        :type handlers: Handler | list[Handler] | None
        :param logging_context: The current logging context. (by default is defaults.DEFAULT_LOGGING_CONTEXT)
        :type logging_context: LoggingContext
        :param group_color: Color of the group. (visible only by using ColoredFormatter)
        :type group_color: str
        :param enabled: If it is set to False, all pinned loggers will not log any messages and all subgroups pinned to
            will be disabled.
        :type enabled: bool
        :param parent_group: Parent of this group. If it is not None, then copies all parameters from that group.
        :type parent_group: Group | str | None
        """

        if parent_group is None:
            self.handlers = [] if handlers is None else (
                [handlers, ] if isinstance(handlers, Handler) else handlers
            )
            self.logging_context  = logging_context
            self.group_color      = group_color
            self.enabled          = enabled
            self.name_path        = name

        else:
            if isinstance(parent_group, str):
                if parent_group not in logging_context.groups_by_name:
                    raise NameError(f'Group "{parent_group}" isn\'t defined in given logging context.')

                parent_group = logging_context.groups_by_name[parent_group]

            self.handlers         = parent_group.handlers
            self.logging_context  = parent_group.logging_context
            self.enabled          = parent_group.enabled
            self.name_path        = parent_group.name_path + '.' + name
            self.group_color      = parent_group.group_color if group_color == '' else group_color

            parent_group.subgroups.append(self)
        self.name                     = name
        self.subgroups: list[Group]   = []
        self.loggers: list['Logger']  = []
        self.parent_group             = parent_group

        self.logging_context.groups.append(self)
        self.logging_context.groups_by_name[name] = self
        update_group_name_offset(self.logging_context)

    def enable(self):
        """Enables this group and all pinned loggers and subgroups."""

        self.enabled = True

        for l in self.loggers:
            l.enable()

        for sg in self.subgroups:
            sg.enable()

    def disable(self):
        """Enables this group and all pinned loggers and subgroups."""

        self.enabled = False

        for l in self.loggers:
            l.disable()

        for sg in self.subgroups:
            sg.disable()

    def subgroup(self, *args, **kwargs):
        """Alternative constructor of the :class:`Group`. But with "parent_group" set to exist instance.
        This method is shorthand for `Group(..., parent_group=self)`. All arguments passed to this function
        is passed to the constructor of the group.

        Example:

        .. code-block:: python

            example_group      = pyrolog.Group('ExampleGroup', handlers=[..., ])
            example_sub_group  = example_group.subgroup()
            example_logger     = example_group.group(name='ExampleLogger', group_color=pyrolog.TextColor.red)
        """
        return Group(*args, **kwargs, parent_group=self)

    def logger(self, *args, **kwargs):
        """Alternative constructor of the :class:`Logger`. But with "group" set to exist instance.
        This method is shorthand for `Logger(..., group=self)`. All arguments passed to this function
        is passed to the constructor of the logger.

        Example:

        .. code-block:: python

            example_group   = pyrolog.Group('ExampleGroup', handlers=[..., ])
            example_logger  = example_group.logger(name='ExampleLogger', logger_color=pyrolog.TextColor.cyan)
        """
        return Logger(*args, **kwargs, group=self)
