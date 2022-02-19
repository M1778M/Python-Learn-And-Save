dictA = {x: x*x for x in (1,2,3,4)}

print(dictA)
print(dict((x, x*x) for x in (1,2,3,4)))

########################################################################

dictB = dict((name,len(name)) for name in ("amir","mohamad",'python','elahe','ali') if len(name)>3)
print(dictB)
