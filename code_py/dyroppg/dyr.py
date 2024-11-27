# Superklasse
class Dyr:
    def __init__(self, navn, alder):
        """
        Initialiserer et Dyr-objekt med navn og alder.
        """
        self.navn = navn
        self.alder = alder

    def spis(self, mat):
        """
        Tar inn et Mat-objekt og returnerer en melding om at dyret spiser.
        """
        return f"{self.navn} spiser {mat.navn} som gir {mat.næringsverdi} energi."

    def __str__(self):
        """
        Returnerer en streng som beskriver dyret.
        """
        return f"Dyr: {self.navn}, Alder: {self.alder}"

    def __eq__(self, other):
        """
        Sjekker om to dyr er like basert på navn og alder.
        """
        return isinstance(other, Dyr) and self.navn == other.navn and self.alder == other.alder


# Subklasse 1: Pattedyr
class Pattedyr(Dyr):
    def __init__(self, navn, alder, pelsfarge):
        super().__init__(navn, alder)
        self.pelsfarge = pelsfarge

    def lyder(self):
        """
        Returnerer lyden til pattedyr.
        """
        return f"{self.navn} lager lyder!"

    def __str__(self):
        return f"Pattedyr: {self.navn}, Alder: {self.alder}, Pelsfarge: {self.pelsfarge}"


# Subklasse 2: Fugl
class Fugl(Dyr):
    def __init__(self, navn, alder, vingespenn):
        super().__init__(navn, alder)
        self.vingespenn = vingespenn

    def fly(self):
        """
        Returnerer en melding om at fuglen flyr.
        """
        return f"{self.navn} flyr med vingespenn på {self.vingespenn} meter!"

    def __str__(self):
        return f"Fugl: {self.navn}, Alder: {self.alder}, Vingespenn: {self.vingespenn}"


# Klasse som brukes av Dyr: Mat
class Mat:
    def __init__(self, navn, næringsverdi):
        """
        Initialiserer Mat-objekt med navn og næringsverdi.
        """
        self.navn = navn
        self.næringsverdi = næringsverdi

    def beskrivelse(self):
        """
        Returnerer en beskrivelse av maten.
        """
        return f"{self.navn} gir {self.næringsverdi} energi."

    def __str__(self):
        return f"Mat: {self.navn}, Næringsverdi: {self.næringsverdi}"

    def __eq__(self, other):
        """
        Sjekker om to matobjekter er like.
        """
        return isinstance(other, Mat) and self.navn == other.navn and self.næringsverdi == other.næringsverdi


# Hovedprogram for å demonstrere klassene
if __name__ == "__main__":
    # Opprett objekter
    banan = Mat("Banan", 50)
    kjøtt = Mat("Kjøtt", 100)

    tiger = Pattedyr("Tiger", 5, "Stripete")
    ørn = Fugl("Ørn", 3, 2.5)

    # Demonstrer metoder
    print(tiger)
    print(ørn)

    print(tiger.spis(banan))
    print(ørn.spis(kjøtt))

    print(tiger.lyder())
    print(ørn.fly())
