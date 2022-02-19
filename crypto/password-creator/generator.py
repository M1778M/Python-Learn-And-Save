import pickle as pk

f = open("sc.passwd",'rb')

alp = 'abcdefghijklmnopqrstuvwxyz'

r1,r2,r3 = pk.load(f)

f.close()

def ref(char):
    return alp[len(alp) - alp.find(char) - 1]

def to_rs():
    global r1,r2,r3
    f1=''
    f2=''
    f3=''
    for i in r1:
        f1 += i
    for i in r2:
        f2 += i
    for i in r3:
        f3 += i
    r1 = f1
    r2 = f2
    r3 = f3


def create(c):
    to_rs()
    c1 = r1[alp.find(c)]
    c2 = r2[alp.find(c1)]
    c3 = r3[alp.find(c2)]
    rf = ref(c3)
    c3 = alp[r3.find(rf)]
    c2 = alp[r2.find(c3)]
    c1 = alp[r1.find(c2)]

    return c1

state = 0
pl = "Hello"

def rot():
    global r1,r2,r3
    r1 = r1[1:] + r1[0]
    if state % 26:
        r2 = r2[1:] + r2[0]
    if state % (26*26):
        r3 = r3[1:] + r3[0]

gt = 1

def get_pass(value):
    pao = ''
    for i in value:
        pao += create(i)
    return pao

def start():
    while gt:
        pao = ''
        get = input("PasswordCreator-/")
        if "pass/" in get:
            if get == "pass/exit":
                exit()
            elif get == "pass/clear":
                from os import system
                system("clear")
                start()
            elif get == "pass/change":
                rot()
                start()
            elif get == "pass/rot":
                rot()
                start()
            
        for c in get:
            pao += create(c)
        print(pao)
        #state += 1
        #rot()
start()
