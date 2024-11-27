import pytest
from dyr import Dyr, Pattedyr, Fugl, Mat

def test_spis():
    mat = Mat("Gras", 20)
    dyr = Dyr("Ku", 3)
    assert dyr.spis(mat) == "Ku spiser Gras som gir 20 energi."

def test_lyder():
    tiger = Pattedyr("Tiger", 5, "Stripete")
    assert tiger.lyder() == "Tiger lager lyder!"

def test_fly():
    fugl = Fugl("Ørn", 3, 2.5)
    assert fugl.fly() == "Ørn flyr med vingespenn på 2.5 meter!"
