# flake8: noqa
class Descriptor:
    def __init__(self):
        self.__fuel_cap = 0
    def __get__(self, instance, owner):    
        return self.__fuel_cap
    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("Fuel Capacity can only be an integer")

        if value < 0:
            raise ValueError("Fuel Capacity can never be less than zero")

        self.__fuel_cap = value

    def __delete__(self, instance):
        del self.__fuel_cap
class Car:
    fuel_cap = Descriptor()
    def __init__(self,make,model,fuel_cap):
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap

    def __str__(self):
        return "{0} model {1} with a fuel capacity of {2} ltr.".format(self.make,self.model,self.fuel_cap)

car2 = Car("BMW","X7",40)
print(car2)
# 40
# BMW model X7 with a fuel capacity of 40 ltr.