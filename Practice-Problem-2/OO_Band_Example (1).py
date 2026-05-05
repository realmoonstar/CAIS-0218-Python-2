#Band's name, year formed, genres, and members can add or remove members by name, and calculate the average age of members.

class Band:

    #Name : String
    #Members : Member[]
    #YearFormed : int
    #Genre : String[]

    def __init__(self, name :str, year :int, genres: list[str]):
        self.__name = name
        self.__year = year
        self.__genres = genres
        self.__members = [] #List of BandMember objects

    def __str__(self) -> str:
        rep = ""
        rep += self.__name + "\n"
        rep += "Year Formed: " + str(self.__year) + "\n"
        rep += "Genres: "
        for g in self.__genres:
            rep += g + " "
        rep += "Members:\n"
        for m in self.__members:
            rep += str(m) + "\n"
        return rep
    # GETTERS
    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def genres(self):
        return self.__genres

    @property
    def members(self):
        return self.__members

    # SETTERS WITH VALIDATION
    @name.setter
    def name(self, newName):
        if newName == "":
            raise Exception("Band name cannot be blank.")
        self.__name = newName

    @year.setter
    def year(self, newYear):
        if newYear < 1900 or newYear > 2026:
            raise Exception("Year formed must be between 1900 and 2026.")
        self.__year = newYear

    @genres.setter
    def genres(self, newGenres):
        if len(newGenres) == 0:
            raise Exception("Band must have at least one genre.")
        self.__genres = newGenres

    # ADD MEMBER
    def addMember(self, member):
        self.__members.append(member)

    # REMOVE MEMBER BY FULL NAME
    def removeMember(self, name):
        for m in self.__members:
            fullName = m.fName + " " + m.lName
            if fullName.lower() == name.lower():
                self.__members.remove(m)
                return True
        return False

    # AVERAGE AGE
    def findAverageAge(self):
        if len(self.__members) == 0:
            return 0
        total = 0
        for m in self.__members:
            total += m.age
        return total / len(self.__members)

        
