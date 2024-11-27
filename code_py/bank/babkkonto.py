class Bankkonto:
    def __init__(self, eier, kontonummer, saldo=0):
        self.eier = eier
        self.kontonummer = kontonummer
        self.saldo = saldo

    def sett_inn_penger(self, amount):
        self.saldo += amount
        print(f"{amount} kr lagt til. Ny saldo: {self.saldo} kr.")

    def ta_ut_penger(self, amount):
        if amount <= self.saldo:
            self.saldo -= amount
            print(f"{amount} kr tatt ut. Ny saldo: {self.saldo} kr.")
        else:
            print("Ikke nok saldo.")

    def vis_saldo(self):
        print(f"Saldo for konto {self.kontonummer}: {self.saldo} kr.")

    # Equality method to compare accounts by account number
    def __eq__(self, other):
        if isinstance(other, Bankkonto):
            return self.kontonummer == other.kontonummer
        return False
