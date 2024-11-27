def bilettpris(alder: int):
    alder = int(input('Your age please: '))
    pris = 0
    if(alder <= 6):
        pris = 0
        print('Du er barn, spør en voksen om bilett')
    if(17 >= alder > 6):
        pris = 63
    if(67 >= alder >= 18):
        pris = 157
    elif(alder > 67):
        pris = 79
    return pris

