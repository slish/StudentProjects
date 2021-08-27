#Oppgave 3: Hund
'''
Klassen Hund blir definert i denne filen, sammen med dens instansvariabler og
-metoder. 
'''
class Hund:
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def hentAlder(self):
        return self._alder

    def hentVekt(self):
        return self._vekt

    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    def spis(self,mat):
        self._metthet += mat
        if self._metthet > 7:
            self._vekt += 1
