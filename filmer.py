import conda

def skriv_favorittfilmer():
    filmer = []
    for i in range(3):
        film = input(f"Skriv inn favorittfilm {i+1}: ")
        filmer.append(film)

    with open("filmer.txt", "w") as fil:
        for film in filmer:
            fil.write(film + "\n")

skriv_favorittfilmer()

def les_og_legg_til_filmer():
    try:
        with open("filmer.txt", "r") as fil:
            filmer = fil.readlines()
            print("Filmer som allerede er lagret:")
            for film in filmer:
                print(film.strip())
    except FileNotFoundError:
        print("Ingen filmer er lagret enda.")

    nye_filmer = []
    antall = int(input("Hvor mange nye filmer vil du legge til? "))
    for i in range(antall):
        ny_film = input(f"Legg til ny film {i+1}: ")
        nye_filmer.append(ny_film)

    with open("filmer.txt", "a") as fil:
        for ny_film in nye_filmer:
            fil.write(ny_film + "\n")

les_og_legg_til_filmer()
