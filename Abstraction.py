from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def moveForward(self):
        pass
    @abstractmethod
    def moveBackward(self):
        pass
    @abstractmethod
    def fm(self):
        pass

class Swift(Car):
    def moveForward(self):
        print("Swift is moving forward!")
    def moveBackward(self):
        print("Swift is moving backward!")
    def fm(self):
        print("Swift is playing fm!")


class Innova(Car):
    def moveForward(self):
        print("Innova is moving forward!")

    def moveBackward(self):
        print("Innova is moving backward!")

    def fm(self):
        print("Innova is playing fm!")

swift=Swift()
swift.moveForward()
swift.moveBackward()
swift.fm()



