import csv
import conda

def les_karakterer(filnavn):
    karakterer = []
    try:
        with open(filnavn, 'r') as fil:
            leser = csv.reader(fil)
            next(leser)  # Hopp over header
            for rad in leser:
                karakterer.append(int(rad[1]))
        return karakterer
    except FileNotFoundError:
        print(f"Filen {filnavn} ble ikke funnet.")
        return []

def regn_ut_gjennomsnitt(karakterer):
    if len(karakterer) == 0:
        return 0
    return sum(karakterer) / len(karakterer)

def skriv_gjennomsnitt(gjennomsnitt, filnavn):
    with open(filnavn, 'w') as fil:
        fil.write(f"Gjennomsnittskarakter: {gjennomsnitt:.2f}")

karakterer = les_karakterer("elever.csv")
gjennomsnitt = regn_ut_gjennomsnitt(karakterer)
skriv_gjennomsnitt(gjennomsnitt, "gjennomsnitt.txt")
print(gjennomsnitt)
