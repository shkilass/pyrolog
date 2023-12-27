
import pyrolog
import math

####

# MAIN

colored_formatter = pyrolog.ColoredFormatter(
    format_string=pyrolog.defaults.COLORED_MAXIMUM_FORMAT_STRING
)

# declare stdout handler with log level - debug
sout_handler = pyrolog.StdoutHandler(
    log_level='debug',
    formatter=colored_formatter
)

# declare file handler with log_level - debug
file_handler = pyrolog.FileHandler(
    'presentation.log',
    log_level='debug',
    formatter=pyrolog.PlainFormatter(
        format_string=pyrolog.defaults.MAXIMUM_FORMAT_STRING
    )
)

# initialize main logger with stdout (console) handler and file handler
main_logger = pyrolog.Logger('MainLogger', handlers=[sout_handler, file_handler])

# examples of the default log levels
main_logger.debug('This is {} message', 'debug')
main_logger.exception('This is {} message', 'exception')
main_logger.info('This is {} message', 'info')
main_logger.warn('This is {} message', 'warn')
main_logger.error('This is {} message', 'error')
main_logger.critical('This is critical message')

# pretty formatting + colored types
main_logger.debug('Int: {} List: {} Dict: {}',
                  13,
                  ['abc', 3.14, False],
                  {'hello': 'world', 'e_is': math.e})
main_logger.exception('Tuple: {} Bool: {} Bytes: {}', ('hello', 'world'), True, b'hex of 255,255,255\x00is\x00\xff\xff\xff')
main_logger.info('Float: {}', math.pi)
main_logger.warn('Exception (formatting only): {}', NameError("name 'abc' is not defined"))

# example of pyrolog.fmt() usage
main_logger.info('{} -- {}', 'pi is', pyrolog.fmt('{:.2f}', math.pi))

# example exception logging
try:
    printt('Hello, world!')
except Exception as e:
    # NOTE: You can use also debug, critical and other log levels to print exceptions
    main_logger.exception('Exception example', exc=e)

main_logger.info('It is continue work')

# uncolored type
main_logger.info('Uncolored float: {} str: {}',
                 pyrolog.Uncolored(math.pi),
                 pyrolog.Uncolored('some string'))

# example with "use_repr"
another_sout_handler = pyrolog.StdoutHandler(
    log_level='debug',
    formatter=pyrolog.ColoredFormatter(
        format_string=pyrolog.defaults.COLORED_MAXIMUM_FORMAT_STRING,
        use_repr=True,
    )
)

# example of the multiple loggers and logger with custom color
another_logger = pyrolog.Logger(
    'AnotherLoggerWithLongName:)',
    logger_color=pyrolog.TextColor.lightmagenta,
    handlers=[another_sout_handler, ]
)

# example of using of the color bindings
another_logger.info('This is {style.bold}another {fore.red}PYROLOG{fore.reset} logger{reset}')
another_logger.info('And it has {fore.black}{bg.yellow}another{bg.reset}{fore.reset} {} with {} parameter enabled', 'ColoredFormatter()', 'use_repr')

# example with the dict
another_logger.debug('Example with the dict: {}',
                     {'hello': {'beautiful': 'world'}, 'e_is': pyrolog.fmt('{:.5f}', math.e)})

# example of the offset between names of the loggers
main_logger.warn('Main logger is {fore.lightred}{style.bold}alive{reset}!! And it has offset')

# example with plain formatter
plain_sout_handler = pyrolog.StdoutHandler(
    log_level='debug',
    formatter=pyrolog.PlainFormatter(
        format_string=pyrolog.defaults.MAXIMUM_FORMAT_STRING
    )
)

plain_logger = pyrolog.Logger('PlainLogger', handlers=[plain_sout_handler, ])

plain_logger.info('There is plain logger, without coloring, but with offsets')

# try to use colors as with main_logger
plain_logger.debug('Try to use {fore.red}colors{fore.reset}')

# disable plain logger
plain_logger.disable()

# these log messages will not be logged because, logger is disabled

plain_logger.debug('am I disabled?..')
plain_logger.critical('Do not disable me!!')

# disable handler of the another logger
another_logger.handlers[0].disable()

# these log messages will not be logged, because handler of this logger is disabled

another_logger.info('Hello, PlainLogger, I got disabled too')
plain_logger.error('But, you enabled... wtf?')
another_logger.debug('My handler is disabled')

####

# GROUPS

# creating simple group

plugins_group = pyrolog.Group(
    name='Plugins',
    handlers=[sout_handler, ],
    group_color=pyrolog.TextColor.red
)

# creating "plugin" loggers
core_plugin_logger        = plugins_group.logger('CorePlugin')
helloworld_plugin_logger  = plugins_group.logger('HelloWorldPlugin')

core_plugin_logger.info('Plugin loaded!')
helloworld_plugin_logger.info('Plugin loaded!')

core_plugin_logger.debug('Pyrolog version: {}', pyrolog.__version__)
helloworld_plugin_logger.info('Hello, world!')

# it saves offsets
main_logger.info('It saves offsets')

# subgroups

core_plugin_subgroup = plugins_group.subgroup(
    name='CorePlugin'
)

core_plugin_logger_auth = core_plugin_subgroup.logger('AuthSystem')

core_plugin_logger_auth.debug('New user authorized with the username {}', 'ftdot')

# many subgroups

many_subgroups = core_plugin_subgroup.subgroup(
    name='Many'
).subgroup(
    name='Sub'
).subgroup(
    name='Groups'
)

idk_how_name_this = many_subgroups.logger('IDKLogger')
idk_how_name_this.info(':)')

# disable main group of many subgroups
core_plugin_subgroup.disable()

idk_how_name_this.info('This will not be logged')

# logger with group by string
some_other_plugin_logger = pyrolog.Logger(name='SomeOtherPlugin', group='Plugins')

some_other_plugin_logger.debug(
    'Some other plugin that uses {} group by passing string to {} argument',
    'Plugins',
    'group'
)

# log only levels demo

only_warns_logger = pyrolog.Logger(
    name='OnlyWarnsLogger',
    handlers=[
        pyrolog.StdoutHandler(
            log_level=pyrolog.LogOnlyLevels(['warn', ]),
            formatter=colored_formatter
        )
    ]
)

only_warns_logger.debug('Level: {}', 'debug')
only_warns_logger.exception('Level: {}', 'exception')
only_warns_logger.info('Level: {}', 'info')
only_warns_logger.warn('Level: {} (This is will be logged)', 'warn')
only_warns_logger.error('Level: {}', 'error')
only_warns_logger.critical('Level: {}', 'critical')

# example use of this feature:

logger = pyrolog.Logger(
    name='SomeLogger',
    handlers=[
        pyrolog.StderrHandler(log_level=pyrolog.LogOnlyLevels(['exception', 'error', 'critical']),
                              formatter=colored_formatter),
        # NOTE: ^^^^^^^^^^^^^ is handler to the stderr.
        pyrolog.StdoutHandler(log_level=pyrolog.LogOnlyLevels(['debug', 'info', 'warn']),
                              formatter=colored_formatter)
    ]
)

logger.info('It message is logged to the stdout')
logger.error('It message is logged to the stderr')

####

# CUSTOM LOG LEVELS

# create custom level
pyrolog.utils.make_new_log_level(
    pyrolog.Logger,  # class
    'trace',         # name of the new log level
    2,               # 5 - debug, trace is lower than debug
)

main_logger.trace('This message will not be logged, {}', 'because main logger is not TRACE log level')

trace_logger = pyrolog.Logger(
    name='TraceLogger',
    handlers=[
        pyrolog.StdoutHandler(
            log_level='trace',
            formatter=colored_formatter,
        )
    ]
)

trace_logger.trace('Level: {}', 'trace')
trace_logger.debug('Level: {}', 'debug')
trace_logger.exception('Level: {}', 'exception')
trace_logger.info('Level: {}', 'info')
trace_logger.warn('Level: {} (This is will be logged)', 'warn')
trace_logger.error('Level: {}', 'error')
trace_logger.critical('Level: {}', 'critical')

####

# CUSTOM COLORS

# copy default color dict
custom_color_dict            = {}
custom_color_dict['types']   = dict(pyrolog.defaults.DEFAULT_COLOR_DICT['types'])
custom_color_dict['levels']  = dict(pyrolog.defaults.DEFAULT_COLOR_DICT['levels'])

custom_color_dict['levels']['trace'] = pyrolog.TextColor.lightgreen

custom_trace_logger = pyrolog.Logger(
    name='TraceLogger',
    handlers=[
        pyrolog.StdoutHandler(
            log_level='trace',
            formatter=pyrolog.ColoredFormatter(
                format_string=pyrolog.defaults.COLORED_MAXIMUM_FORMAT_STRING,
                color_dict=custom_color_dict,
            ),
        )
    ]
)

custom_trace_logger.trace('Trace has a new color now')

trace_logger.trace('But only for one logger (formatter)')

# globally create custom color
pyrolog.defaults.DEFAULT_COLOR_DICT['levels']['trace'] = pyrolog.TextColor.lightgreen

trace_logger.trace('But after update of the global color dict, {} has own color', 'trace')

####

main_logger.info('🔥 {style.bold}Pyrolog{reset} - Best pretty logging library')
