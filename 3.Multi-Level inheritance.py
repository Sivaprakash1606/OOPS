# -> Multi-Level Inheritance:
class Vehicle: # Parent Class
    no_of_wheels=4
    def moveForward(self):
        print("Vehicle is moving Forward")

class Car(Vehicle): # Child class / Sub class
    no_of_airbags=5

class Maruthi(Car):
    mileage=25.0

car1=Maruthi()
print(car1.no_of_wheels)
car1.moveForward()
print(car1.no_of_airbags)
print(car1.mileage)

