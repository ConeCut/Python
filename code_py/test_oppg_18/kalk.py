class Kalkulator:
    @staticmethod
    def pluss(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def minus(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def gange(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def dele(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Kan ikke dele på null!")
        return a / b
