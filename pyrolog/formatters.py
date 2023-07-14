
import traceback
import datetime

from abc import abstractmethod
from collections import namedtuple
from functools import lru_cache

from . import empty_colors
from .logging_context import LoggingContext
from ._types import VarDict, ColorDict
from .defaults import (DEFAULT_LOGGING_CONTEXT,
                       MINIMAL_FORMAT_STRING,
                       MINIMAL_TIME_FORMAT_STRING,
                       COLORED_MINIMAL_FORMAT_STRING,
                       COLORED_MINIMAL_TIME_FORMAT_STRING,
                       DEFAULT_COLOR_DICT)
from .colors import TextColor, BGColor, TextStyle

from typing import Any

__all__ = ['fmt', 'Uncolored', 'Formatter', 'PlainFormatter', 'ColoredFormatter']

fmt = namedtuple('FormatTuple', ('format_string', 'string'))

####


class Uncolored:

    def __init__(self, value: Any):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

####


class Formatter:

    def __init__(self,
                 format_string: str = MINIMAL_FORMAT_STRING,
                 time_format_string: str = MINIMAL_TIME_FORMAT_STRING,
                 static_variables: VarDict | None = None,
                 logging_context: LoggingContext = DEFAULT_LOGGING_CONTEXT
                 ):
        self._format_string      = format_string
        self.time_format_string  = time_format_string
        self.static_variables    = {} if static_variables is None else static_variables
        self.logging_context     = logging_context

        self.time_formatting = '{time}' in self.format_string

        defined_formatters.append(self)

    @property
    def format_string(self):
        return self._format_string

    @format_string.setter
    def format_string(self, value: str):
        self._format_string   = value
        self.time_formatting  = '{time}' in value

    def add_static_variable(self, name: str, value: Any):
        self.static_variables[name] = value

    def del_static_variable(self, name: str) -> bool:
        if name in self.static_variables:
            del self.static_variables[name]
            return True
        return False

    @abstractmethod
    def format(self,
               message: str,
               time: datetime.datetime | None,
               level: str,
               logger_color: str,
               logger_name: str,
               group_name: str,
               group_color: str,
               fmt_args: list[Any],
               fmt_kwargs: dict[str, Any]
               ):
        raise NotImplementedError('Method "format()" isn\'t implemented')

    @abstractmethod
    def format_exception(self, exc: Exception):
        raise NotImplementedError('Method "format_exception()" isn\'t implemented')

    @abstractmethod
    def format_time(self, time: datetime.datetime | None):
        raise NotImplementedError('Method "format_time()" isn\'t implemented')


class PlainFormatter(Formatter):

    def __init__(self, *args: Any, offsets: bool = True, **kwargs: dict[str, Any]):

        super().__init__(*args, **kwargs)

        self.offsets                                 = offsets
        self.static_variables['level_offset']        = self.logging_context.get_level_offset() if offsets else 0
        self.static_variables['logger_name_offset']  = self.logging_context.get_logger_name_offset() if offsets else 0
        self.static_variables['group_name_offset']   = self.logging_context.get_group_name_offset() if offsets else 0
        self.static_variables['fore'] = empty_colors.EmptyTextColor
        self.static_variables['bg'] = empty_colors.EmptyBGColor
        self.static_variables['style'] = empty_colors.EmptyTextStyle
        self.static_variables['reset'] = ''

    def format_message(self,
                       message: str,
                       level: str,
                       logger_color: str,
                       logger_name: str,
                       group_name: str,
                       group_color: str,
                       fmt_args: list[Any],
                       fmt_kwargs: dict[str, Any]):
        return message.format(
            level=level,
            logger_color=logger_color,
            logger_name=logger_name,
            group_name=group_name,
            group_color=group_color,
            *fmt_args,
            **fmt_kwargs,
            **self.static_variables,
        )

    def format(self,
               message: str,
               time: datetime.datetime | None,
               level: str,
               logger_color: str,
               logger_name: str,
               group_name: str,
               group_color: str,
               fmt_args: list[Any],
               fmt_kwargs: dict[str, Any]
               ):
        return self.format_string.format(
            message=self.format_message(
                message,
                level,
                logger_color,
                logger_name,
                group_name,
                group_color,
                fmt_args,
                fmt_kwargs
            ),
            time=self.format_time(time) if self.time_formatting else '*',
            level=level,
            logger_color=logger_color,
            logger_name=logger_name,
            group_name=group_name,
            group_color=group_color,
            *fmt_args,
            **fmt_kwargs,
            **self.static_variables,
        )

    def format_exception(self, exc: Exception):
        return ''.join(traceback.format_exception(exc))[:-1]

    def format_time(self, time: datetime.datetime | None):
        if time is None:
            return ''

        return self.time_format_string.format(
            year=time.year,
            month=time.month,
            day=time.day,
            hour=time.hour,
            minute=time.minute,
            second=time.second,
            microsecond=time.microsecond,  # str(time.microsecond)[:4]
        )


class ColoredFormatter(PlainFormatter):

    def __init__(self,
                 format_string: str = COLORED_MINIMAL_FORMAT_STRING,
                 time_format_string: str = COLORED_MINIMAL_TIME_FORMAT_STRING,
                 *args: Any,
                 color_dict: ColorDict = DEFAULT_COLOR_DICT,
                 use_repr: bool = False,
                 **kwargs: dict[str, Any]):
        super().__init__(format_string, time_format_string, *args, **kwargs)
        self.color_dict  = color_dict
        self.use_repr    = use_repr

        self.static_variables['fore']          = TextColor
        self.static_variables['bg']            = BGColor
        self.static_variables['style']         = TextStyle
        self.static_variables['reset']         = TextStyle.reset

        self._func = repr if use_repr else str

    def get_level_color(self, level: str):
        if level in self.color_dict['levels']:
            return self.color_dict['levels'][level]
        else:
            return ''

    def get_value_color(self, type_: type):
        if type_ in self.color_dict['types']:
            return self.color_dict['types'][type_]
        elif isinstance(type_, Exception):
            return self.color_dict['types']['exception']
        else:
            return self.color_dict['types']['all']

    def format_value(self, value: Any):
        if isinstance(value, fmt):
            value_color = self.get_value_color(type(value[1]))
            return value_color + value[0].format(value[1])

        elif isinstance(value, list):
            list_color = self.get_value_color(list)
            output = f'{list_color}['
            temp = [self.format_value(v) for v in value]
            output += f'{list_color}, '.join(temp) + f'{list_color}]{TextStyle.reset}'

            return output

        elif isinstance(value, tuple):
            tuple_color = self.get_value_color(tuple)
            output = f'{tuple_color}('
            temp = [self.format_value(v) for v in value]
            output += f'{tuple_color}, '.join(temp) + f'{tuple_color}){TextStyle.reset}'

            return output

        elif isinstance(value, dict):
            dict_color = self.get_value_color(dict)
            output = f'{dict_color}{{'
            temp = [f'{self.format_value(k)}{dict_color}: {self.format_value(v)}' for k, v in value.items()]
            output += f'{dict_color}, '.join(temp) + f'{dict_color}}}{TextStyle.reset}'

            return output

        elif isinstance(value, Uncolored):
            return self._func(value) + TextStyle.reset

        return self.get_value_color(type(value)) + self._func(value) + TextStyle.reset

    def format_message(self,
                       message: str,
                       level: str,
                       level_color: str,
                       logger_color: str,
                       logger_name: str,
                       group_name: str,
                       group_color: str,
                       fmt_args: list[Any],
                       fmt_kwargs: dict[str, Any]):
        return message.format(
            level=level,
            level_color=level_color,
            logger_color=logger_color,
            logger_name=logger_name,
            group_name=group_name,
            group_color=group_color,
            *fmt_args,
            **fmt_kwargs,
            **self.static_variables,
        )

    def format(self,
               message: str,
               time: datetime.datetime | None,
               level: str,
               logger_color: str,
               logger_name: str,
               group_name: str,
               group_color: str,
               fmt_args: list[Any],
               fmt_kwargs: dict[str, Any]
               ):
        colored_args    = [self.format_value(a) for a in fmt_args]
        colored_kwargs  = {k: self.format_value(v) for k, v in fmt_kwargs.items()}
        level_color     = self.get_level_color(level)

        return self.format_string.format(
            message=self.format_message(
                message,
                level,
                level_color,
                logger_color,
                logger_name,
                group_name,
                group_color,
                colored_args,
                colored_kwargs
            ),
            time=self.format_time(time) if self.time_formatting else '*',
            level=level,
            level_color=level_color,
            logger_color=logger_color,
            logger_name=logger_name,
            group_name=group_name,
            group_color=group_color,
            *colored_args,
            **colored_kwargs,
            **self.static_variables,
        ) + TextStyle.reset

    def format_exception(self, exc: Exception):
        return self.color_dict['types']['exception'] + ''.join(traceback.format_exception(exc))[:-1]

    def format_time(self, time: datetime.datetime | None):
        if time is None:
            return ''

        return self.time_format_string.format(
            year=time.year,
            month=time.month,
            day=time.day,
            hour=time.hour,
            minute=time.minute,
            second=time.second,
            microsecond=time.microsecond,  # str(time.microsecond)[:4]
            **self.static_variables,
        )

defined_formatters: list[Formatter] = []
