from timeit import timeit

def lp1():
    [x for x in range(100)]

def lp2():
    mylist = []
    for x in range(100):
        if x>10:
            mylist.append(x)

def lp3():
    mylist = []
    for x in range(100):
        if x>10:
            pass



print(timeit("lp1()", setup="from __main__ import lp1"))
print(timeit("lp2()", setup="from __main__ import lp2"))
print(timeit("lp3()", setup="from __main__ import lp3"))
