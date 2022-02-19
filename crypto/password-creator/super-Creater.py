import random
import pickle as pk


alp = 'abcdefghijklmnopqrstuvwxyz'


r1 = list(alp)
random.shuffle(r1)
r1 == ''.join(r1)

r2 = list(alp)
random.shuffle(r2)
r2 == ''.join(r2)

r3 = list(alp)
random.shuffle(r3)
r3 == ''.join(r3)

f = open("sc.passwd",'wb')


pk.dump((r1,r2,r3),f)

f.close()

