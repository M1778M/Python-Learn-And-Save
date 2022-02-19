import numpy as np

a = np.array([[1,2],[3,4]]) # یک عری  in list[]

b=np.matrix([[5,6],[7,8]]) # یک ماتریکس in list[]

print(a) # print the array
print(b) # print the matrix

print()

print(a@a) # or np.dot(a,a) #-> ضرب سطر اول در سطر دوم و تشکیل یک سطر
print(np.dot(b,b))# up^

print()

print(np.multiply(a,a)) # or a*a #-> ضرب عضو در خودش
print(np.multiply(b,b)) # or b*b #-> ضرب عضو در خودش


print()

print(np.prod(a))

