import os
os.getcwd()

os.listdir()
os.listdir("C:\\python-3.9.5")
os.mkdir("new dir")
os.makedirs("newdir\\mother")
os.rmdir("new dir")
os.rmdir("newdir\\mother")
os.removedirs("newdir\\mother")
os.stat("colors.py")
print(os.stat("colors.py").st_type)
####################
import datetime
TS = os.stat("colors.py").st_mtime

print(datetime.datetime.fromtimestamp(TS))
######################

os.path.join()
addr = "C:\\users\\m1778\\Desktop"
file_name = "\\text.py"
os.path.exists(addr+file_name)
######################
os.path.join(addr,file_name)

os.path.join("C:","Users")

os.path.basename(addr)

os.path.dirname("C:\\drivers.html")



