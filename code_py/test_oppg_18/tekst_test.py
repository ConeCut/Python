from tekst import TekstInfo

def test_finn_antall_tegn():
    assert TekstInfo.finn_antall_tegn("Hei verden") == 10

def test_finn_antall_ord():
    assert TekstInfo.finn_antall_ord("Hei verden") == 2

def test_finn_lengste_ord():
    assert TekstInfo.finn_lengste_ord("Hei verden") == "verden"

def test_finn_korteste_ord():
    assert TekstInfo.finn_korteste_ord("Hei verden") == "Hei"
