class Person:
    def __init__(self, navn: str, skole: str, fag: list, klasse: str):
        self.navn  = navn
        self.skole = skole
        self.fag = fag
        self.klasse = klasse
    
    def legg_til_fag(self):
        self.fag = []
        
    def visInfo(self, klasse: list, navn: str, skole: str, fag: list):
        self.navn  = navn
        self.skole = skole
        self.klasse  = klasse
        self.fag = fag
        
    def bytteskole(self, nyskole: str):  
        self.skole = nyskole
        
    def showInfo(self):
        return f"Navn: {self.navn} \nSkole: {self.skole} \nFag: {self.fag} \nKlasse: {self.klasse}"

    
        
    
        

    
        
    
        
        
    
