import os
from colorama import init, Fore, Back, Style

# essential for Windows environment
init()
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
Black = '\x1b[30m'
Red = '\x1b[31m'
Pink = '\x1b[35m'
Yellow = '\x1b[33m'
Gray = '\x1b[37m'
Green = '\x1b[32m'
Blue = '\x1b[34m'
Blue2 = '\x1b[36m'
BGWhite = '\x1b[7m'
BGBlack = '\x1b[40m'
BGPink = '\x1b[41m'
BGGreen = '\x1b[42m'
BGYellow = '\x1b[43m'
BGBlue = '\x1b[44m'
BGPerple = '\x1b[45m'
BGBlue2 = '\x1b[46m'
BGGray = '\x1b[47m'
LGText = '\x1b[52m'
LGText2 = '\x1b[51m'
BIG = '\x1b[1m'
FIT = '\x1b[3m'
TU_ = '\x1b[4m'
TO_ = '\x1b[9m'
TU__ = '\x1b[21m'
