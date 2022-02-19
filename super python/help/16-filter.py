dostan = ['ali','amir','mohamad','reza','farbod','mamadreza','maryam']

def longName(name):
    return len(name)>4
print("map:")
print(list(map(longName,dostan)))
print("filter:")
print(list(filter(longName,dostan)))
print("listComprition:")
print([name for name in dostan if len(name)>4])
################################################
adad = [10,20,35,64,98,51,37,73]

def zog(adadd):
    if adadd%2 == 0:
        return zog

print(list(filter(zog,adad)))
