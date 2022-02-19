list1 = [10,20,50,32]
list2 = [70,80,90,100]
list3 = [200,500,10,8]

def avar(*args):
    return sum(args)/len(args)

print(list(map(avar,list1,list2,list3)))

dostan = ['amir','amin','reza']
def salam(*args):
    for i in args:
        return ('salam be ' + i)

print(list(map(salam,dostan)))