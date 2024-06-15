'''
Object-Oriented Methodology:

1. Object orientation is a software development methodology that is
based on modeling a real-world system.

2. An object-oriented program consits of classes and Objects.
'''

'''
Characteristics:
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism
'''

'''
EXAMPLE:
Class -> Fruit:
       Apple,Orange ->Objects
'''

#Example 1:
class Laptop:
    name=""
    processor=""
    price=0

#Object
hp=Laptop()
dell=Laptop()

hp.name="HP"
hp.processor="i5"
hp.price=50000

dell.name="DELL"
dell.processor="i7"
dell.price=70000

print(hp.price)
print(dell.price)


#Example2:
class Car:  #class contains data members -> member variable,member method
    no_of_wheels=0
    mileage=0.0
    no_of_airbags=0
    def moveForward(self):
        print("Car is Moving!")
    def moveBackward(self):
        print("Car is Moving Backward!")

car1=Car() #instance of a class -object:Instantiation
car2=Car()

car1.no_of_wheels=4
car1.no_of_airbags=4
car1.mileage=25.0
car2.no_of_wheels=4
car2.no_of_airbags=5
car2.mileage=30.0

print(car1.mileage)
car1.moveForward()
print(car2.mileage)
car2.moveBackward()



