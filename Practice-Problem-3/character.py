#char class problem 1
class character:
    def __init__(self, name, character_class, level, health):
        if name == "":
            raise ValueError("name cannot be blank")
        if character_class == "":
            raise ValueError("character_class cannot be blank")
        if level < 1:
            raise ValueError("level must be >= 1")
        if health < 0:
            raise ValueError("health must be >= 0")
        self._name = str(name)
        self.character_class = character_class
        self._level = int(level)
        self._health = int(health)
        

    #1st setter & getter for naame
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("new name cant be blank")
        else:
            self._name = str(new_name)
            
    #2nd setter & getter for level
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, new_level):
        if new_level < 1:
            print("level cannot be less than 1")
        else:
            self._level = new_level

# health getter/setter
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
        else:
            self._health = int(new_health)
            
    #add attack 
    def attack(self):
        return("general attack")
            
#CUSTOM METHODS:
    
    #take dam func
    def take_damage(self, amount):
        if amount < 0:
            print("amount must be >=0")
            return
        self._health -= amount
        if self._health < 0:
            self._health = 0
            print("Nooo " + self._name + " died :(")
            
    #healing func
    def heal(self, amount):
        if amount < 0:
            print("amount must be >=0")
            return
        self._health += amount

    #lvl up func
    def level_up(self):
        self._level += 1
        self._health += 10
        
    #to str output
    def __str__(self):
        return ("Name: "+self._name + "\tClass: " + self.character_class+ "\tLevel: "
                + str(self._level)+ "\tHealth: "+str(self._health))     
