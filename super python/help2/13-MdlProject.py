import pyfiglet as pf
from colorama import init,Fore,deinit
init()
message=input('Enter Message: ')

finishname = Fore.GREEN + pf.figlet_format(message) + Fore.RESET

NoneSpace = '\x20'
print(finishname)