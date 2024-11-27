from babkkonto import Bankkonto
from sparekonto import Sparekonto
from BSUkonto import BSUKonto

def test_bankkonto():
    print("Testing Bankkonto...")
    konto1 = Bankkonto("Ola Nordmann", "12345", 1000)
    konto1.sett_inn_penger(500)  
    konto1.ta_ut_penger(200)     
    konto1.vis_saldo()         
    assert konto1.saldo == 1300, "Bankkonto saldo test failed."
    print("Bankkonto tests passed.\n")

def test_sparekonto():
    print("Testing Sparekonto...")
    sparekonto = Sparekonto("Kari Nordmann", "54321", 5000, uttak_grense=2)
    sparekonto.ta_ut_penger(1000)  
    sparekonto.ta_ut_penger(1000)   
    sparekonto.ta_ut_penger(1000)  
    sparekonto.vis_saldo()         
    assert sparekonto.saldo == 3000, "Sparekonto saldo test failed."
    print("Sparekonto tests passed.\n")

def test_bsu_konto():
    print("Testing BSUKonto...")
    bsu_konto = BSUKonto("Petter Pettersen", "67890", 8000)
    bsu_konto.ta_ut_penger()   
    bsu_konto.ta_ut_penger()     
    bsu_konto.vis_saldo()         
    assert bsu_konto.saldo == 0, "BSUKonto saldo test failed."
    print("BSUKonto tests passed.\n")

def test_equality():
    print("Testing equality...")
    konto1 = Bankkonto("Ola Nordmann", "12345", 1000)
    konto2 = Bankkonto("Ola Nordmann", "12345", 2000)
    konto3 = Bankkonto("Kari Nordmann", "54321", 1500)

    assert konto1 == konto2, "Equality test failed: konto1 and konto2 should be equal."
    assert konto1 != konto3, "Equality test failed: konto1 and konto3 should not be equal."
    print("Equality tests passed.\n")

# Run all tests
if __name__ == "__main__":
    test_bankkonto()
    test_sparekonto()
    test_bsu_konto()
    test_equality()
    print("All tests completed successfully.")



