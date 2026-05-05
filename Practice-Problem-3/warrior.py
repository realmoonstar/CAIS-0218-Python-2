# Defines Warrior and Mage classes that inherit from Character and add armor or mana with custom methods
# and overrides also defines a Guild class that manages members, supports adding/removing by name,
# and displays all members.

#import parent class from problem 1
from character import character

#warrior class problem 2
class warrior(character):
    def __init__(self, name, level, health, armor):
        super().__init__(name, "Warrior",level, health)
        if armor < 0:
            raise ValueError ("You need armor!")
        self._armor = int(armor)

    #getter//setter for armor
    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, new_armor):
        if new_armor < 0:
            print("You need armor!")#must be >= 0
        else:
            self._armor = int(new_armor)
    
    #override ride to str from super
    def __str__(self):
        return super().__str__() + "\tArmor: "+ str(self._armor)

    #shield block method
    def shield_block(self):
        message = self.name +" used shield"
        return message
    
        #add attack 
    def attack(self):
        return("physical attack")

#mage class inherits char
class mage(character):
    def __init__(self, name, level, health, mana):
        super().__init__(name, "Mage", level, health)
        if mana < 0: # must be >= 0
            raise ValueError("you need mana!")
        self._mana = int(mana)

    #getter//setter for mana
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            raise ValueError("you need mana!")#must be >=0
        else:
            self._mana = new_mana

    #add attack 
    def attack(self):
        return("magical attack")
    
    #cast spell method
    def cast_spell(self):
        if self._mana >= 10:
            self._mana -= 10
            return "oh no! "+self.name+" mana reduced by 10"
        else:
            return "Not enough mana"
        
    #override to str from super
    def __str__(self):
        return super().__str__() + "\tMana: "+ str(self._mana)


#guild class
class guild:
    def __init__(self, guild_name):
        self.guild_name = guild_name
        self.members = []#list of character objects,  starts empty

 #add member method       
    def add_member(self, character):
        self.members.append(character)
    
#remove member method
    def remove_member(self, name):
        for char in self.members:
            if char.name.lower() == name.lower():
                self.members.remove(char)
                return
        return "name error"
        
#show member method
    def show_members(self):
        print(self.guild_name+" Members: ")
        for member in self.members:
            print (member)
        
#to str
    def __str__(self):
        return "\nGuild: "+ self.guild_name+ "\t"+"Members: "+str(len(self.members))
