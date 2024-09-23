# create a function that takes two numbers as parameters and returns their sum 
def getNumber(num1,num2):
    res=num1+num2
    return res
res1=getNumber(33,44)
print(res1)

# polymorphism in function 
# write a function multiply that multiplies two numbers,but can also accept and multiply strings
def multiply_numbers(number1,number2):
    res2=number1*number2
    return res2
print(multiply_numbers("string",5))
print(multiply_numbers(2,"string"))
print(multiply_numbers(55,77))

# create a function that returns both the area and circumference of a circle given its radius.
import math
def area_circumference(radius):
    area=math.pi*radius*radius
    circum=2*math.pi*radius
    return area,circum
area1,circum1=area_circumference(10)
print(f"the value is {round(area1,3)},{round(circum1,4)}")
# write a function that greets a user.if no name is provided,it should greet with a default value

def get_default(name="Binod"):
    return f"hello,i am {name}"
print(get_default("saroj"))