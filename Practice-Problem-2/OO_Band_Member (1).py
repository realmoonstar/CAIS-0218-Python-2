# Defines a BandMember with first name, last name, instrument, and date of birth
# includes getters and setters with validation, calculates age, and formats member info in __str__.

from datetime import date

class BandMember:

    def __init__(self, fName: str, lName: str, instrument:str, dateOfbirth:int):
        self._fName = fName
        self._lName = lName
        self._instrument = instrument
        self._dateOfbirth = dateOfbirth

    def __str__(self):
        rep = ""
        rep += self._fName + " " + self._lName + "\tInstrument: " + self._instrument + " " + str(self._dateOfbirth)
        return rep

    @property
    def fName(self) -> str:
        return self._fName
    @property
    def lName(self) -> str:
        return self._lName
    @property
    def instrument(self) -> str:
        return self._instrument

    @property
    def dateOfbirth(self) -> int:
        return self._dateOfbirth

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self._dateOfbirth

    @fName.setter
    def fName(self, newName: str) -> None:
        if len(newName) == 0:
            raise Exception("First name cannot be blank.")
        self._fName = newName
    @lName.setter
    def lName(self, newName: str) -> None:
        if len(newName) == 0:
            raise Exception("Last name cannot be blank.")
        self._lName = newName
    @instrument.setter
    def instrument(self, newInstrument: str) -> None:
        if len(newInstrument) == 0:
            raise Exception("Instrument cannot be blank.")
        self._instrument = newInstrument

    @dateOfbirth.setter
    def dateOfbirth(self, newDob: str):
        if newDob > date.today().year:
            raise Exception("Birth date cannot be in the future.")
        self._dateOfbirth = newDob


def main():

    kirk = BandMember("Kirk", "Hammet", "Guitar", 1962)
    lars = BandMember("Lars", "Ulrich", "Drums", 1963)
    james = BandMember("James", "Hetfield", "Guitar", 1963)
    rob = BandMember("Rob", "Trujilo", "Bass", 1964)

    bandList = [kirk, lars, james, rob]
    for x in bandList:
        print(x)

    rob.lName = "Trujillo"
    print("Updated rob object:\n", rob)
    print("Trying to delete Lars instrument...")
    lars.instrument = ""

main()
