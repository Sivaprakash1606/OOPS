class Father:
    hair_color="white"
    def music(self):
        print("Kuthu Paatu!")
class Mother:
    hair_color="black"
    def music(self):
        print("Melody Paatu")

class child(Father,Mother):
    no_of_legs=2

child1=child()
child1.music()
