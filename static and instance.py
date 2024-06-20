class Person:
    sleepingtime=8 #class variable
    def __init__(self,name,age):
        self.name=name #instance Variable
        self.age=age
    @staticmethod
    def sleep(): # static method  is used to access only static method or static variable
        print("Person should sleep for",Person.sleepingtime,"hrs")
        #OR
    @classmethod
    def sleep1(cls): # Class method
        print("Person should sleep for", cls.sleepingtime, "hrs")

    #instance method
    def eat(self): # But Instance method  is used to access Both static and instance variable,method
        print(Person.sleepingtime)


person1=Person("Siva",22)
person2=Person("A",23)
print(person1.sleepingtime)
person1.sleepingtime=10
print(person1.sleepingtime)
print(Person.sleepingtime)
print(person2.sleepingtime)
Person.sleep()
Person.sleep1()

