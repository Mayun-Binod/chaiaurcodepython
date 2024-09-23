# demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes,but with different behaviours
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    
    def getFullName(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand +"!"
    def fuel_type(self):
        return "petrol or diesel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "electric charge"
e=ElectricCar("tuto","twm","20wh")
print(e.fuel_type())

c=Car("bmw22","xyzbrand")
print(c.fuel_type())