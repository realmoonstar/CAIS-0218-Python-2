#import parent class from problem 1+ child classes from problem 2
from character import character
from warrior import warrior,mage, guild


#problem 3 add archer child class derived from character parent class
class archer(character):
    def __init__(self, name, level, health, arrows):
        super().__init__(name, "Archer",level, health)
        self.arrows = arrows

    #attack method
    def attack(self,):
        return ("ranged attack")

    def __str__(self):
        return super().__str__() + "\tArrows: "+ str(self.arrows)






