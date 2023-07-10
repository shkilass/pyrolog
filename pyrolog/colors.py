
import sys

from colorama import Fore, Back, Style, init, just_fix_windows_console

if sys.platform == 'win32' and '--pyrolog-windows-fix' in sys.argv:
    init()
    just_fix_windows_console()

__all__ = ['TextColor', 'BGColor', 'TextStyle']


class TextColor:
    """Bindings to colorama Fore colors"""

    reset         = Fore.RESET
    black         = Fore.BLACK
    red           = Fore.RED
    green         = Fore.GREEN
    blue          = Fore.BLUE
    cyan          = Fore.CYAN
    yellow        = Fore.YELLOW
    magenta       = Fore.MAGENTA
    white         = Fore.WHITE
    lightblack    = Fore.LIGHTBLACK_EX
    lightred      = Fore.LIGHTRED_EX
    lightgreen    = Fore.LIGHTGREEN_EX
    lightblue     = Fore.LIGHTBLUE_EX
    lightcyan     = Fore.LIGHTCYAN_EX
    lightyellow   = Fore.LIGHTYELLOW_EX
    lightmagenta  = Fore.LIGHTMAGENTA_EX
    lightwhite    = Fore.LIGHTWHITE_EX


class BGColor:
    """Bindings to colorama Back colors"""

    reset = Back.RESET
    black = Back.BLACK
    red = Back.RED
    green = Back.GREEN
    blue = Back.BLUE
    cyan = Back.CYAN
    yellow = Back.YELLOW
    magenta = Back.MAGENTA
    white = Back.WHITE
    lightblack = Back.LIGHTBLACK_EX
    lightred = Back.LIGHTRED_EX
    lightgreen = Back.LIGHTGREEN_EX
    lightblue = Back.LIGHTBLUE_EX
    lightcyan = Back.LIGHTCYAN_EX
    lightyellow = Back.LIGHTYELLOW_EX
    lightmagenta = Back.LIGHTMAGENTA_EX
    lightwhite = Back.LIGHTWHITE_EX


class TextStyle:
    """Bindings to colorama Style"""

    reset   = Style.RESET_ALL
    dim     = Style.DIM
    bold    = Style.BRIGHT
    normal  = Style.NORMAL
