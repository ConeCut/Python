class Deltaker:
    def __init__(self, navn):
        self.navn = navn

    def vis_info(self):
        return f"Deltaker: {self.navn}"

class Lag:
    def __init__(self, navn):
        self.navn = navn
        self.deltakere = []
        self.poeng = 0 

    def legg_til_deltaker(self, deltaker):
        self.deltakere.append(deltaker)

    def vis_info(self):
        deltakere_info = ", ".join([d.vis_info() for d in self.deltakere])
        return f"Lag: {self.navn}, Poeng: {self.poeng}\nDeltakere: {deltakere_info}"

    def oppdater_poeng(self, poeng):
        self.poeng += poeng

class Turnering:
    def __init__(self):
        self.lag = []

    def legg_til_lag(self, lag):
        self.lag.append(lag)

    def registrer_kamp(self, lag1, lag2, poeng_lag1, poeng_lag2):
        lag1.oppdater_poeng(poeng_lag1)
        lag2.oppdater_poeng(poeng_lag2)
        print(f"Kamp registrert: {lag1.navn} ({poeng_lag1} poeng) vs {lag2.navn} ({poeng_lag2} poeng)")

    def rangert_liste(self):
        self.lag.sort(key=lambda lag: lag.poeng, reverse=True)
        print("Rangert liste:")
        for i, lag in enumerate(self.lag, start=1):
            print(f"{i}. {lag.navn} - {lag.poeng} poeng")


turnering = Turnering()

lag1 = Lag("Lyn")
lag1.legg_til_deltaker(Deltaker("Ola"))
lag1.legg_til_deltaker(Deltaker("Kari"))

lag2 = Lag("Tornado")
lag2.legg_til_deltaker(Deltaker("Per"))
lag2.legg_til_deltaker(Deltaker("Anna"))

turnering.legg_til_lag(lag1)
turnering.legg_til_lag(lag2)

turnering.registrer_kamp(lag1, lag2, 3, 1)
turnering.registrer_kamp(lag1, lag2, 1, 2)

turnering.rangert_liste()
