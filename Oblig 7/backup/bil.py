class Bil:

    def __init__(self, merke, modell, hk):
        self._merke = merke
        self._modell = modell
        self._km = 0
        self._hestekrefter = hk

    def tut(self):
        print("Tuuuut!")

    def kjor(self, km):
        self._km += km

    def trim(self, faktor):
        self._hestekrefter *= faktor

    def __str__(self):
        return f"Merke: {self._merke}\nModell: {self._modell}\nKM-stand: {self._km}km\nHestekrefter: {self._hestekrefter}hk"