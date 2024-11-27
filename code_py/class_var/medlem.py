class Medlem:
    id = 0
    
    def __init__(self, fornavn, etternavn, alder):
        self._fornavn = fornavn
        self.etternavn = etternavn
        self._alder = alder
        Medlem.id += 1
        self._id = Medlem.id    
        
    def getId(self):
        return self._id 
    
    def getName(self):
        return self._fornavn
    
    def visMedlem(self):
        print(f"Yuh")
    
    def __eq__(self, other):
        return (self.etternavn == other.etternavn) and (self._fornavn == other._fornavn)
        
