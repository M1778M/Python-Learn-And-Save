from socket import *

ip = input("ip: ")


for i in range(1,256):

    try:
        live = gethostbyaddr(ip+str(i))
        print("ip live: ",ip+str(i)," ",live)
    except:
        print("None")