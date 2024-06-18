# Example 1: Multiple inheritance :
class Father:
    color_of_hair="white"
class Mother:
    color_of_eyes="blue"
    color_of_hair="black"
class child(Father,Mother):
    no_of_legs=2

child1=child()
print(child1.color_of_hair)
print(child1.color_of_eyes)
print(child1.no_of_legs)

# Example 2: Diamond problem in Multiple inheritance
class Vechile:
    no_of_wheels=4
    def moveForward(self):
        print("Vechicle is moving Forward")
class Car(Vechile):
    no_of_airbags=5

class Maruthi(Car):
    mileage=25.0

class Toyoto(Car):
    mileage=30.0

class Toythi(Maruthi,Toyoto):  #(Ambiguty)
    has_Touchscreen=True

car1=Toythi()
print(car1.no_of_wheels)
car1.moveForward()
print(car1.no_of_airbags)
print(car1.mileage)
print(car1.has_Touchscreen)

