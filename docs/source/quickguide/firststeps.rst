.. _firststeps:

.. currentmodule:: pyrolog

===========
First steps
===========

To install this library, simply type this command (Windows variant):

.. code-block:: shell

    $ pip install pyrolog

On linux systems, you must use ``pip3`` instead of. Command:

.. code-block:: shell

    $ pip3 install pyrolog

Formatters
----------

Formatters allow us to pretty format our logs. Library has these formatters by default:
``PlainFormatter`` - only plain text, ``ColoredFormatter`` - colored logs.

Formatters has some options as:

.. code-block:: python
    
    * format string - String responsible for formatting.
    * time format string - String responsible for formatting time.
    * static variables - Static variables, that can be used by {...} syntax.
    * logging context - Current logging context.
    * offsets - enable\disable offsets.

About the format strings, by default there has many variants, see
:module:`pyrolog.defaults`.

To use handlers, you must firsly create formatter instance!

Handlers
--------

To create a handler for the stdout (console output) you can use
:class:`pyrolog.handlers.StdoutHandler`.

.. code-block:: python

    import pyrolog

    # NOTE: Exception is a log level little than info.
    #       It recommended to use it for exception logging.
    stdout_handler = pyrolog.StdoutHandler(
        log_level='exception',
        formatter=pyrolog.ColoredFormatter(pyrolog.defaults.COLORED_TIMED_MINIMAL_FORMAT_STRING),
    )

.. note:: You can also use :class:`pyrolog.utils.LogLevel` to set the ``log_level``
    parameter.

There also have support for **file handler**. This class named as
:class:`pyrolog.handlers.FileHandler`.

.. code-block:: python

    import pyrolog

    file_handler = pyrolog.FileHandler(
        'logs/{timestamp}.log', # filename
        timestamp=True, # enables {timestamp} feature
        log_level='debug', # log level
        formatter=pyrolog.PlainFormatter(pyrolog.defaults.TIMED_MINIMAL_FORMAT_STRING),
    )

Lets combine them into one code:

.. code-block:: python

    import pyrolog

    stdout_handler  = pyrolog.StdoutHandler(
        log_level='exception',
        formatter=pyrolog.ColoredFormatter(pyrolog.defaults.COLORED_TIMED_MINIMAL_FORMAT_STRING),
    )
    file_handler    = pyrolog.FileHandler(
        'logs/{timestamp}.log', # filename
        timestamp=True, # enables {timestamp} feature
        log_level='debug', # log level
        formatter=pyrolog.PlainFormatter(pyrolog.defaults.TIMED_MINIMAL_FORMAT_STRING),
    )

Our first handlers are done.

Logger group
------------

Lets create our first logger group. Group contains all parameters for child
loggers. This is useful in case of multiple loggers usage. To create it, you
can use :class:`pyrolog.loggergroup.Group`.

You can create loggers without groups.

Create **MyApp** group:

.. code-block:: python

    import pyrolog

    myapp_group = pyrolog.Group('MyApp')

.. seealso:: You can see it reference: :class:`pyrolog.loggergroup.Group`

Lets add our loggers by examples above to this group.

.. note:: Handlers can be pinned to groups by ``handlers`` parameter.
    This parameter is named and takes ``Handler | list[Handler]`` type.
    Example is bottom.

.. code-block:: python

    import pyrolog

    # Our first handlers for stdout and file
    stdout_handler  = pyrolog.StdoutHandler(
        log_level='exception',
        formatter=pyrolog.ColoredFormatter(pyrolog.defaults.COLORED_TIMED_MINIMAL_FORMAT_STRING),
    )
    file_handler    = pyrolog.FileHandler(
        'logs/{timestamp}.log', # filename
        timestamp=True, # enables {timestamp} feature
        log_level='debug', # log level
        formatter=pyrolog.PlainFormatter(pyrolog.defaults.TIMED_MINIMAL_FORMAT_STRING),
    )

    # Our first group by name MyApp
    myapp_group = pyrolog.Group('MyApp', handlers=[stdout_handler, file_handler])

Our first group done!

Logging
-------

Loggers can be created by :class:`pyrolog.logger.Logger` class. It, how as a
logger groups, takes a ``handlers`` parameter. But, as I said, if you use
logger group, it stores all parameters for child loggers and set it automatically.
All that required from Loggers is a ``group`` parameter. To get more info
see Loggers reference (just click on :class:`pyrolog.logger.Logger`).

.. code-block:: python

    import pyrolog

    # Our first handlers for stdout and file
    stdout_handler  = pyrolog.StdoutHandler(
        log_level='exception',
        formatter=pyrolog.ColoredFormatter(pyrolog.defaults.COLORED_TIMED_MINIMAL_FORMAT_STRING),
    )
    file_handler    = pyrolog.FileHandler(
        'logs/{timestamp}.log', # filename
        timestamp=True, # enables {timestamp} feature
        log_level='debug', # log level
        formatter=pyrolog.PlainFormatter(pyrolog.defaults.TIMED_MINIMAL_FORMAT_STRING),
    )

    # Our first group by name MyApp
    myapp_group = pyrolog.Group('MyApp', handlers=[stdout_handler, file_handler])

    # Create a Main logger that includes MyApp group
    logger = pyrolog.Logger('Main', group=myapp_group)

Our logger is done! Now, we can log messages to it. By default, logger
hasn't ``debug``, ``exception``, ``info`` and other methods. It adds via
:func:`pyrolog.logger.Logger.bind_log_methods()`. This methods calls by default,
and uses this list of the log levels -> ``pyrolog.defaults.DEFAULT_LOG_LEVELS``
:module:`pyrolog.defaults`.

List of all the default log levels:

.. code-block:: python
    * debug      (int value: 1)
    * exception  (int value: 2)
    * info       (int value: 5)
    * warning    (int value: 10)
    * error      (int value: 15)
    * critical   (int value: 20)
    * notset     (int value: 9999)


.. code-block:: python

    number1 = 15
    logger.debug('Defined number 1: {}', number1)

    number2 = 2
    logger.debug('Defined number 2: {}', number2)

    result = number1 + number2
    logger.info('Adding number 1 to number2. Result: {}', result)

.. note:: To log methods you can pass format variables as long as you need.

You can also use all features of the python string formatting.

.. warning:: All

.. code-block:: python

    import math

    logger.info('{:<20}--{:>19}', 'pi is', f'{math.pi:.2f}')

Code above will produce info log with message: ``pi is  --  3.14``.

Log exceptions
--------------

All methods of logging are defines named parameter ``exception=``. It
takes any exception and log it after the message.

.. code-block:: python

    try:
        printt('Hello, world!')
    except Exception as e:
        # You can use any function to log exception. But, recommended to use
        # only exception level for exceptions.

        logger_main.debug('An exception occurred: {}', e, exc=e)
        logger_main.exception('An exception occurred: {}', e, exc=e)
        logger_main.info('An exception occurred: {}', e, exc=e)
        logger_main.warning('An exception occurred: {}', e, exc=e)
        logger_main.error('An exception occurred: {}', e, exc=e)
        logger_main.critical(f'An exception occurred: {e}', exc=e)
