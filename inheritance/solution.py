# create an ElectricCar class that inherits from the Car class and has an additional attibute battery_size
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    
    def getFullName(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand +"!"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
e=ElectricCar("tuto","twm","20wh")
print(e.model)
print(e.brand)
print(e.getFullName())
c=Car("toyota","bmwmodel")
print(c.brand)
print(c.model)
print(c.getFullName())

print(e.get_brand())