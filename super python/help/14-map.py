names = ['amir','ali','reza','gholam']
map1 = map(len,names)
print(map1)
print(list(map1))
#######################################3

print([len(item) for item in names])
number = [1,2,5,654,76,23,9]

def ToThis(num):
    return (num * 0.01)
map2 = map(ToThis,number)
print(list(map2))