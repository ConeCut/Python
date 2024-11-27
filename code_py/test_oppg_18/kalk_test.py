from kalk import Kalkulator

def test_pluss():
    assert Kalkulator.pluss(2, 3) == 5

def test_minus():
    assert Kalkulator.minus(5, 3) == 2

def test_gange():
    assert Kalkulator.gange(2, 3) == 6

def test_dele():
    assert Kalkulator.dele(6, 3) == 2
    try:
        Kalkulator.dele(6, 0)
    except ValueError as e:
        assert str(e) == "Kan ikke dele på null!"
