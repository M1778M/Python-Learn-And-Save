import random as rand

from requests import get as GET_URL_PRT,post as POST_URL_PRT


myl = ['mamad','reza','gholam','sara']
print(rand.randint(1,100))
print(rand.choice(myl))


def circle(r):
    pi = 3.14
    return r*r*pi
    
    