from colorama import init, Fore, Back, Style

# essential for Windows environment
init()
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

Black = '\033[30m'
Red = '\033[31m'
Pink = '\033[35m'
Yellow = '\033[33m'
Gray = '\033[37m'
Green = '\033[32m'
Blue = '\033[34m'
Blue2 = '\033[36m'
BGWhite = '\033[7m'
BGBlack = '\033[40m'
BGPink = '\033[41m'
BGGreen = '\033[42m'
BGYellow = '\033[43m'
BGBlue = '\033[44m'
BGPerple = '\033[45m'
BGBlue2 = '\033[46m'
BGGray = '\033[47m'
LGText = '\033[52m'
LGText2 = '\033[51m'
BIG = '\033[1m'
FIT = '\033[3m'
TU_ = '\033[4m'
TO_ = '\033[9m'
TU__ = '\033[21m'
s = '\x1a'
