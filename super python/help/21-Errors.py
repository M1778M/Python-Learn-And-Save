# class myerror(Exception):
#     pass
# try:
#     raise myerror("my error is raised")
# except myerror as e:
#     print("Error14")
#
# class Error1002(ValueError):
#     pass
#
# def func(x):
#     if x<0:
#         raise Error1002("Adad vared shode manfi ast")
#
#
# func(-2)

#Try Except finally
try:
    a = 2/0
    print(a)
except ZeroDivisionError as e:
    print(e)
else:
    print("start")

# finally:
#     print("zero division started")

def f_to_z(fard):
    if fard % 2 != 1:
        raise ValueError("adad vared shode fard nist!!!")
    return fard + 1
print(f_to_z(2))