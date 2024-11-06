from another_day_in_paradise import Person

class Elev(Person):
    def __init__(self, navn: str, skole: str, fag: list, klasse: str):
        super().__init__(navn, skole, fag, klasse)

    def bytteklasse(self, nyklasse: str):
        self.klasse  = nyklasse
        
    def showInfo(self):
        return super().showInfo() + f"\nKlasse: {self.klasse}"