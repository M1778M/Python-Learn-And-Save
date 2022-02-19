#try:
#    print(test)
#except:
#    print('an Error Maked')
    
    
per = {'name' : 'mamad'}
try:
    print(per['age'])
except ValueError:
    print(None)
except KeyError:
    print(None)
else:
    print('This is else')
finally:
    print('This is a finally')