class Vehicle: # Parent Class
    no_of_wheels=4
    def moveForward(self):
        print("Vehicle is moving Forward")

class Car(Vehicle): # Child class / Sub class
    no_of_airbags=5

car1=Car()
print(car1.no_of_wheels)
print(car1.no_of_airbags)
car1.moveForward()






