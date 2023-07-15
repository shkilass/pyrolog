"""Contains empty version of the color bindings of the colorama library. See :mod:`pyrolog.colors`.

.. important::
    Due to the library's import system, if you import `pyrolog` by this code:

    .. code-block:: python

        import pyrolog

    You must use this as:

    .. code-block:: python

        pyrolog.empty_colors.EmptyTextColor

    As example.
"""


class EmptyTextColor:
    """Empty variant of :class:`pyrolog.TextColor`."""

    reset         = ''
    black         = ''
    red           = ''
    green         = ''
    blue          = ''
    cyan          = ''
    yellow        = ''
    magenta       = ''
    white         = ''
    lightblack    = ''
    lightred      = ''
    lightgreen    = ''
    lightblue     = ''
    lightcyan     = ''
    lightyellow   = ''
    lightmagenta  = ''
    lightwhite    = ''


class EmptyBGColor:
    """Empty variant of :class:`pyrolog.BGColor`."""

    reset         = ''
    black         = ''
    red           = ''
    green         = ''
    blue          = ''
    cyan          = ''
    yellow        = ''
    magenta       = ''
    white         = ''
    lightblack    = ''
    lightred      = ''
    lightgreen    = ''
    lightblue     = ''
    lightcyan     = ''
    lightyellow   = ''
    lightmagenta  = ''
    lightwhite    = ''


class EmptyTextStyle:
    """Empty variant of :class:`pyrolog.TextStyle`."""

    reset   = ''
    dim     = ''
    bold    = ''
    normal  = ''
