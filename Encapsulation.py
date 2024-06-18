#Encapsulation:

#Binding of Variables and Methods

#Getters and Setters

#Access Modifier:
#1. default -> Public
#2. __ -> Private
#3. _ -> Protected

class Car:
    mileage=9
    def __init__(self,car_name,no_of_wheels,no_of_airbags,mileage):
        self.car_name=car_name
        self.__no_of_wheels=no_of_wheels
        self.no_of_airbags=no_of_airbags
        self.mileage=mileage

    #getter
    def get_no_of_wheels(self):
        return self.__no_of_wheels

    #setter
    def set_no_of_wheels(self,no_of_wheels):
        self.__no_of_wheels=no_of_wheels

car1=Car("Maruthi",4,4,25.0)
print(car1.get_no_of_wheels())
car1.set_no_of_wheels(8)
print(car1.get_no_of_wheels())
