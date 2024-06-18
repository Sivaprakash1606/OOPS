# Polymorphism:
# Poly -> Many
# morphism -> Forms
      # # Method Overloading or Compile time Polymorphism # #
# Another program example:
class Summation:

    '''
    int sum(int a, int b):
       return a+b

    float sum(float a, float b):
       return a+b

    int sum(int a,int b,int c):
       return a+b+c

    sum(1,2)
    sum(1,2,3)
    sum(1.0,2.0)
    '''

    # In Python Method-Overloading is directly not possible, Otherwise
    #How to use in python:

    #example 1 -> 1st way :

    def summ(self,a,b,c=0,d=0):
        return a+b+c+d

    # example 2 -> 2nd way:

    def summ(self,*args):
        ans=0
        for i in args:
            ans+=i
        return ans

summation=Summation()
print(summation.summ(1,2,3,4,5))



