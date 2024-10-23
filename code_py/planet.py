from classes_objects import Planet

def printMeAPlanet():
    thisone = Planet('thisone', 0, 1)
    thatone = Planet('thatone', 2, 3)
    thoseones = Planet('thoseones', 4, 5)
    
    thisone.myFunc()
    thatone.myFunc()
    thoseones.myFunc()
    
printMeAPlanet()