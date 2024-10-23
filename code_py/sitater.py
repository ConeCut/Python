def les_sitater(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            sitater = fil.readlines()
            print(f"Antall sitater: {len(sitater)}\n")
            for sitat in sitater:
                print(sitat.strip())
    except FileNotFoundError:
        print(f"Filen {filnavn} ble ikke funnet.")

les_sitater("sitater.txt")
