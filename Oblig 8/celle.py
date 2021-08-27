from random import randint

#Celleklassen inneholder status om cellene og metoder for å hente status og returnere tegnet til cellen for å tegne det på spillebrettet.
class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "Doed"

    # Endre status
    def settDoed(self):
        self._status = "Doed"

    def settLevende(self):
        self._status = "Levende"

    # Hente status
    def erLevende(self):
        return self._status == "Levende"

    #hentStatusTegn tegner cellene basert på valget til brukeren og om cellen er levende eller død
    def hentStatusTegn(self,choice):
        sign = "."
        signList = ["☺","♦","§","O","r"]
        if self.erLevende():
            if signList[choice] == "r":
                sign = signList[randint(0,3)]
            else:
                sign = signList[choice]
        return sign
