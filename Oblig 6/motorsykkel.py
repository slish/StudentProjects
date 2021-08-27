#Oppgave 1: Motorsykkel
'''
Filen inneholder klassen Motorsykkel og dens instansvariabler og -metoder. 
'''
class Motorsykkel:
    def __init__(self,merke,regNr, kilometerStand):
        self._merke = merke
        self._regNr = regNr
        self._kilometerstand = kilometerStand

    def kjor(self,km):
        self._kilometerstand += km

    def hentKilometerstand(self):
        return self._kilometerstand

    def skrivUt(self):
        print("Merke: " + self._merke + "\nRegistreringsnummer: " + self._regNr + "\nKilometerstand: " + str(self._kilometerstand))
