from another_day_in_paradise import Person

class Larer(Person):
    def __init__(self, navn: str, skole: str, fag: list, klasse: str, lonn: float, lonnstilleg: float, kontaktlarer: bool):
        super().__init__(navn, skole, fag)
        self.klasse = klasse
        self.lonn = lonn
        self.lonnstillegg = lonnstilleg
        self.kontaktlarer = kontaktlarer

    def bytteklasse(self, nyklasse: str):
        self.klasse  = nyklasse
        
    def showInfo(self):
        return super().showInfo() + f"Lonn: {self.lonn} \nLonnstillegg: {self.lonnstillegg} \nKontaktlarer: {self.kontaktlarer}"