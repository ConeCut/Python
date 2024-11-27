class TekstInfo:
    @staticmethod
    def finn_antall_tegn(tekst: str) -> int:
        return len(tekst)

    @staticmethod
    def finn_antall_ord(tekst: str) -> int:
        return len(tekst.split())

    @staticmethod
    def finn_lengste_ord(tekst: str) -> str:
        return max(tekst.split(), key=len)

    @staticmethod
    def finn_korteste_ord(tekst: str) -> str:
        return min(tekst.split(), key=len)
