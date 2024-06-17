# Constructor and Destructor:
class car:
    def __init__(Aself,car_name,no_of_wheels,no_of_airbags,mileage=10.0):
        print("This is Constructor")
        Aself.no_of_wheels=no_of_wheels
        Aself.no_air_bags=no_of_airbags
        Aself.mileage=mileage
        Aself.car_name=car_name
    def __del__(Aself):
        print("This is a Destructor!",Aself)
        print("This is a Destructor!", id(Aself))

    def __str__(Aself):
        return Aself.car_name

    def moveForward(Aself,speed):
        print("Car is moving with a speed",speed,"Km.")

    def moveBackward(Aself):
        print("Car is moving Backward")


car1=car("Minicooper",4,4,25.0)
print(car1)
print(car1.car_name,car1.no_of_wheels,car1.no_air_bags,car1.mileage)
car1.moveForward(45)

car2=car("Benz",5,5)
print(car2)
print(car2.car_name,car2.no_of_wheels,car2.no_air_bags,car2.mileage)
car1.moveBackward()

