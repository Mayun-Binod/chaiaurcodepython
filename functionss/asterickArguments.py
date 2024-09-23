# # write a function that takes variable number of arguments and returns their sum.
def sum1(*args):
    print(*args)
print(sum1(1,2,3,4,5))

def sum2(*args):
    print(*args)
    print(args) # prints in tuple
print(sum2(10,11,22,44))

def sum3(*args):
    print(*args)
    print(args) # prints in tuple
    return sum(args) # build in function is sum
print(sum3(23,10,11,22,44))

def sum4(*args):
    print(*args)
    print(args) # prints in tuple
    print(args[2])
    print(args[3])
print(sum2(10,11,22,44,45,67))


def sum4(*args):
    print(*args)
    print(args) # prints in tuple
    print(args[2])
    print(args[3])
    for storeAegs in args:
        print(storeAegs*4)
print(sum4(10,11,22,44,45,67))


def sumValues(*args):
    print(args)
    sumval=0
    for getsum in args:
        # print(getsum)
        sumval=sumval+getsum
        print(sumval)
        return sumval    
print(sumValues(10,11,22,33,44,55,66,77))