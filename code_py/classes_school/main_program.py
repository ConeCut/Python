from another_day_in_paradise import Person
from elev import Elev
from larer import Larer

def hovedprogram():
    elev1 = Elev("Per", "Kuben", ["IT2", "Norsk"], "Matte")
    elev1.bytteklasse('Norsk')
    
    print(elev1.showInfo())
    
hovedprogram()