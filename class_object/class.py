class Car:
    brand=None
    model=None
c1=Car()
print(c1)

class Student:
    def __init__(self,name1,age1):
        self.name=name1
        self.age=age1
    
    def getFullName(self):
        return f"{self.name} {self.age}"
s=Student("binod",23)
print(s.name)
print(s.age)
print(s.getFullName())

s1=Student("safari",23)
print(s1.name)
print(s1.age)