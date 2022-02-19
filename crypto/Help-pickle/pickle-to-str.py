import pickle as pk

f = open("data.dat",'rb')

f.seek(0)

print(pk.load(f))

f.close()