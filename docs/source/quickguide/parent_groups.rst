.. _parent_groups:

.. currentmodule:: ezlog

=============
Parent groups
=============

Lets explain code bottom.

.. code-block:: python

    import pyrolog

    # declare stdout handler with log level - debug
    file_handler = pyrolog.FileHandler(
        'example.log',
        log_level='debug',
        formatter=pyrolog.PlainFormatter(pyrolog.defaults.MAXIMUM_TIME_FORMAT_STRING),
    )
    sout_handler = pyrolog.StdoutHandler(
        log_level='info',
        formatter=pyrolog.ColoredFormatter(pyrolog.defaults.COLORED_MAXIMUM_TIME_FORMAT_STRING),
    )  # recommended: exception log level as default

    # initialize example groups
    example_group = pyrolog.Group('Example', handlers=[sout_handler, file_handler])
    groups_group = pyrolog.Group('Groups', parent=example_group)
    subgroup_group = groups_group.subgroup('Subgroup')

    main_logger = pyrolog.Logger('Main', group=subgroup_group)

    # examples of the default log levels
    main_logger.debug('This is {} message', 'debug')
    main_logger.exception('This is {} message', 'exception')
    main_logger.info('This is {} message', 'info')
    main_logger.warning('This is {} message', 'warning')
    main_logger.error('This is {} message', 'error')
    main_logger.critical('This is critical message')

As you can see, this is very simple! All groups takes parameter ``parent``.
You can create as many as you need the groups via parent. Child groups copy
all parameters from parent group as loggers from groups.

See :class:`pyrolog.group.Group`
