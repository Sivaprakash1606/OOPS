# # Method Overriding or Runtime Polymorphism
class Father:
    def __init__(self):
        print("Father Constructor")
    def say_hello(self):
        print("Hello from Father!")

class child(Father):
    def __init__(self):
        print("Child Constructor")
    def say_hello(self, name):
        print("Hello from child!", name)

child1 = child()
child1.say_hello("siva")
