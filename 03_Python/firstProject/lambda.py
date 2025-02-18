def Sum(a,b):
    return a+b
print(Sum(4,5))

mySum=lambda a,b:a+b
print(mySum(4,21))
print((lambda a,b: a+b)(2,4))

# def power(x):
#     return lambda n:x**n
# print(power(4)(2))

def sqeure(x):
    return x**2
def cube(x):
    return x**3
def absolute(x):
    if x>0:
        return x
    else:
        return -(x)
    
def Hof(type):
    if type=='sqeure':
        return sqeure
    if type=='cube':
        return cube
    if type=='absolute':
        return absolute

res=Hof('sqeure')
print(res(6))