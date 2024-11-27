from babkkonto import Bankkonto

class Sparekonto(Bankkonto):
    def __init__(self, eier, kontonummer, saldo=0, uttak_grense=12):
        super().__init__(eier, kontonummer, saldo)
        self.uttak_grense = uttak_grense
        self.uttak_performed = 0

    def ta_ut_penger(self, amount):
        if self.uttak_performed < self.uttak_grense:
            super().ta_ut_penger(amount)
            self.uttak_performed += 1
        else:
            print("Uttaksgrense nådd.")
