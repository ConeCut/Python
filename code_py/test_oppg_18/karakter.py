def karakter(poengsum: int) -> str:
    if poengsum < 50:
        return "Ikke bestått"
    elif 50 <= poengsum <= 69:
        return "Bestått"
    elif 70 <= poengsum <= 89:
        return "Godt bestått"
    elif 90 <= poengsum <= 100:
        return "Meget godt bestått"
    else:
        return "Ikke gyldig poengsum!"
