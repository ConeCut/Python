# Les inn den første datoen
dag1 = int(input("Skriv inn dag for første dato: "))
mnd1 = int(input("Skriv inn måned for første dato: "))

# Les inn den andre datoen
dag2 = int(input("Skriv inn dag for andre dato: "))
mnd2 = int(input("Skriv inn måned for andre dato: "))

# Sammenlign datoene
if mnd1 < mnd2 or (mnd1 == mnd2 and dag1 < dag2):
    print("Riktig rekkefølge!")
elif mnd1 == mnd2 and dag1 == dag2:
    print("Samme dato!")
else:
    print("Feil rekkefølge!")
