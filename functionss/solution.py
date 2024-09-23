# write a function to calculate and return the square of a number.
def get_calculate():
    user=int(input("enter the square of a number:")) # calling in user function
    print(f"the square of a number is {user**2}")
print(get_calculate())

# without user normal function
def getCalculate(square):
    result=square**4
    print(f"the square is {result}")
print(getCalculate(5))

# return function
def returnSquare(squares):
    res=squares**7
    return res
res1=returnSquare(10) # return 10000000 not None
print(res1) 