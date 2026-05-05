# Runs the main program for Practice Problem 
#creates Character, Warrior, Mage, and Archer objects,  a battle round, displays class‑specific details, adds all characters to a Guild, and prints
# the guild and its members.

from character import character
from warrior import warrior,mage, guild
from attack import archer

#problem set 3 main program
def battle_round(characters):
    for member in characters:
        print(member.attack())


def show_class_details(characters):
    for c in characters:
        if isinstance(c, warrior):
            print(c.name + " Armor: " + str(c.armor))
        elif isinstance(c, mage):
            print(c.name + " Mana: " + str(c.mana))
        elif isinstance(c, archer):
            print(c.name + " Arrows: " + str(c.arrows))
        elif isinstance(c, character):
            print(c.name + ": NPC")
        
def main():
    #3 Character objects calling the constructors!! :)
    c1 = character("Bob", "NPC", 10, 100)
    w1 = warrior("Amy", 10, 100, 50)
    m1 = mage("Fred", 10, 100, 50)
    a1 = archer("Rob", 10, 100, 50)
    #3 objects stored in list
    guildList = [c1,w1,m1,a1]
    battle_round(guildList)
    show_class_details(guildList)

    g1 = guild("First Guild")
    for char in guildList:
        g1.add_member(char)
    print (g1)
    g1.show_members()
main()
