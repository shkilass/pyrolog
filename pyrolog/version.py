"""This module contains version information of the library.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.__version__

    As example.

    Also, `VersionInfo` isn't imports by default. You can't use it with code like this:

    .. code-block:: python

        pyrolog.VersionInfo

    See below for details how to use it, if you really want this.
"""

from collections import namedtuple

__all__ = ['__version__', '__version_tuple__', '__version_info__']

VersionInfo = namedtuple('VersionInfo', ['major', 'minor', 'patch', 'release_level', 'commit'])
"""Named tuple type.

.. warning::
    This isn't imports by default! You can import this by using this code:
    
    .. code-block:: python
    
        from pyrolog.version import VersionInfo
"""

__version__ = "2.3.0"
"""String with the current version of the library"""

__version_tuple__ = (2, 3, 0)
"""Tuple with the current version of the library"""

__version_info__ = VersionInfo(*__version_tuple__, 'release', 'a6c699f')
"""Named tuple with the current version + technical details of the library release"""
