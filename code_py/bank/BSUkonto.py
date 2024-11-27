from babkkonto import Bankkonto
 
class BSUKonto(Bankkonto):
    def ta_ut_penger(self):
        if self.saldo > 0:
            print(f"Tar ut alle pengene: {self.saldo} kr.")
            self.saldo = 0
        else:
            print("Ingen penger på kontoen.")
