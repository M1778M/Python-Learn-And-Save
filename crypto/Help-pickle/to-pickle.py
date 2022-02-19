import pickle as pk

a = [1,2,3,4]

f = open("data.dat",'wb')

pk.dump(a,f)

f.close()








