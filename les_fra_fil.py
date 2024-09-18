def les_fra_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            innhold = fil.read()
            print(innhold)
    except FileNotFoundError:
        print(f"Filen {filnavn} finnes ikke.")

filnavn = input("Skriv inn filnavn: ")
les_fra_fil(filnavn)
