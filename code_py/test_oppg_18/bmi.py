def bmi_klassifisering(hoyde: float, vekt: float) -> str:
    bmi = vekt / (hoyde ** 2)
    if bmi <= 18.4:
        return "Undervekt"
    elif 18.5 <= bmi <= 24.9:
        return "Normalvekt"
    elif 25 <= bmi <= 29.9:
        return "Overvekt"
    elif 30 <= bmi <= 34.9:
        return "Fedme, grad 1"
    elif 35 <= bmi <= 39.9:
        return "Fedme, grad 2"
    else:
        return "Fedme, grad 3"
