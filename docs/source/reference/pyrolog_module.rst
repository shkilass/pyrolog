.. _pyrolog_mod:

.. currentmodule:: pyrolog

=======
Library
=======

.. important::
    Imports ``pyrolog.group``, ``pyrolog.logger``, ``pyrolg.logging_context``,
    ``pyrolog.handlers``, ``pyrolog.formatters``, ``pyrolog.version``, ``pyrolog.colors``
    must be used without the ``.group``, ``.logger``, ``.logging_context``, etc. prefixes
    if you use ``import pyrolog``. These modules imports as ``from .MOD import *``.
    
    Other modules: ``pyrolog.defaults``, ``pyrolog.types``, ``pyrolog.utils``, ``pyrolog.
    empty_colors`` must be imported as is.

pyrolog
-------

.. automodule:: pyrolog
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.version
---------------

.. automodule:: pyrolog.version
    :members:
    :undoc-members:
    :show-inheritance:

    .. autodata:: VersionInfo
    .. autodata:: __version__
    .. autodata:: __version_tuple__
    .. autodata:: __version_info__

pyrolog.logging_context
-----------------------

.. automodule:: pyrolog.logging_context
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.group
-------------

.. automodule:: pyrolog.group
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.logger
--------------

.. automodule:: pyrolog.logger
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.handlers
----------------

.. automodule:: pyrolog.handlers
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.formatters
------------------

.. automodule:: pyrolog.formatters
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.utils
-------------

.. automodule:: pyrolog.utils
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog._types
--------------

.. automodule:: pyrolog._types
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.colors
--------------

.. automodule:: pyrolog.colors
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.empty_colors
--------------------

.. automodule:: pyrolog.empty_colors
    :members:
    :undoc-members:
    :show-inheritance:

pyrolog.defaults
----------------

.. automodule:: pyrolog.defaults
    :no-undoc-members:

    .. autodata:: DEFAULT_LOG_LEVELS
    .. autodata:: MINIMAL_FORMAT_STRING
    .. autodata:: TIMED_MINIMAL_FORMAT_STRING
    .. autodata:: MINIMAL_TIME_FORMAT_STRING
    .. autodata:: MAXIMUM_TIME_FORMAT_STRING
    .. autodata:: MAXIMUM_TIME_FORMAT_STRING_FILENAME_SAFE
    .. autodata:: MAXIMUM_FORMAT_STRING
    .. autodata:: DEFAULT_LOGGING_CONTEXT
    .. autodata:: DEFAULT_COLOR_DICT
    .. autodata:: COLORED_MINIMAL_FORMAT_STRING
    .. autodata:: COLORED_TIMED_MINIMAL_FORMAT_STRING
    .. autodata:: COLORED_MINIMAL_TIME_FORMAT_STRING
    .. autodata:: COLORED_MAXIMUM_TIME_FORMAT_STRING
    .. autodata:: COLORED_MAXIMUM_FORMAT_STRING
