
# telefonbok.py
telefonbok = {
    "Arne": 22334455,
    "Lisa": 95959595,
    "Jonas": 97959795,
    "Peder": 12345678
}

navn = input("Skriv inn et navn: ")

if navn in telefonbok:
    print(f"{navn}s telefonnummer er {telefonbok[navn]}")
else:
    nummer = input(f"Telefonnummer til {navn} er ikke i telefonboka. Vennligst oppgi nummeret: ")
    telefonbok[navn] = int(nummer)
    print(f"{navn} ble lagt til i telefonboka med nummer {telefonbok[navn]}")

# lek_med_ordboker.py
meg = {
    "Navn": "Ditt navn",
    "Alder": 18,
    "By": "Din by",
    "Interesser": ["programmering", "fotball", "lesing"]
}

for nøkkel, verdi in meg.items():
    print(f"{nøkkel}: {verdi}")

vaer = {}
vaer["Dato"] = "25.09.2024"
vaer["Maks temperatur"] = 15
vaer["Min temperatur"] = 8
vaer["Nedbør"] = 3
vaer["Vindstyrke"] = 5

print(f"I dag er det {vaer['Dato']}. Maks temperatur er {vaer['Maks temperatur']}°C, "
      f"min temperatur er {vaer['Min temperatur']}°C. Det kommer til å regne {vaer['Nedbør']}mm, "
      f"og vindstyrken vil være {vaer['Vindstyrke']}m/s.")

python_ordbok = {
    "variabel": "En plassholder for en verdi.",
    "datatype": "En type data, som heltall, flyttall, tekst, etc.",
    "operator": "En symbol som utfører en operasjon, som +, -, *, /.",
    "løkke": "En måte å kjøre kode flere ganger på."
}

for begrep, forklaring in python_ordbok.items():
    print(f"{begrep}: {forklaring}")

# teori.txt (only answers)

# a) Liste (ord)
# b) Mengde (streng)
# c) Liste (streng)
# d) Ordbok (streng)
# e) Ordbok (heltall)
# f) Liste (heltall)

# bil.py
def les_bil(filnavn):
    resultat = {}
    with open(filnavn, 'r') as fil:
        for linje in fil:
            linje = linje.strip()
            nøkkel, verdi = linje.split(":")
            resultat[nøkkel] = verdi
    return resultat

bil_data = les_bil("bil.txt")
print(bil_data)

# song_contest.py
def les_song_contest(filnavn):
    årene = []
    landene = []
    with open(filnavn, 'r') as fil:
        for linje in fil:
            linje = linje.strip()
            år, land = linje.split(" ", 1)
            årene.append(år)
            landene.append(land)

    song_contest = {"år": årene, "land": landene}
    return song_contest

song_data = les_song_contest("song_contest.txt")
print(song_data)

# poeng.py
def les_poeng(filnavn):
    poeng = {}
    with open(filnavn, 'r') as fil:
        for linje in fil:
            linje = linje.strip()
            navn, score_str = linje.split(":")
            poeng[navn] = [int(p) for p in score_str.split(",")]
    return poeng

poeng_data = les_poeng("poeng.txt")
print(poeng_data)

def les_poeng_sum(filnavn):
    poeng = {}
    with open(filnavn, 'r') as fil:
        for linje in fil:
            linje = linje.strip()
            navn, score_str = linje.split(":")
            poeng[navn] = sum([int(p) for p in score_str.split(",")])
    return poeng

poeng_sum_data = les_poeng_sum("poeng.txt")
print(poeng_sum_data)
