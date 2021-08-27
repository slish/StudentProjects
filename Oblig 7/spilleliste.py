#Filen definerer klassen Spilleliste og funksjonene som tilhører denne.

from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        file = open(filnavn, "r")
        for lines in file:
            sang = lines.rstrip("\n").split(";")
            self._sanger.append(Sang(sang[1],sang[0])) #Artist og tittel blir lest inn fra listen i motsatt rekkefølge fra oppgaven, for å kunne stemme overens med test-filene

    def leggTilSang(self,nySang):
        self._sanger.append(nySang)

    def spillSang(self,sang):
        sang.spill()

    def spillAlle(self):
        for song in self._sanger:
            Spilleliste.spillSang(self,song)

    def fjernSang(self,sang):
        pop = -1
        popCheck = False
        for songs in self._sanger:
            if popCheck == False:
                pop += 1
            if songs.sjekkArtistOgTittel(sang._artist,sang._tittel):
                popCheck = True
        if popCheck == True:
            self._sanger.pop(pop) #Fjerner det liste-elementet hvor vi finner både et ord fra artist og tittel via sjekkArtistOgTittel-funksjonen

    def finnSang(self,tittel):
        value = None
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                value = sang
        return value

    def hentArtistUtvalg(self,artistnavn):
        artistListe = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                artistListe.append(sang)
        return artistListe

    def __str__(self):
        for object in self._sanger:
            artistStr = " ".join([
                word.capitalize()
                for word in object._artist
                ])
            tittelStr = " ".join([
                word.capitalize()
                for word in object._tittel
                ])
            print(f"{artistStr} - {tittelStr}")
        return f"Liste ferdig"  #Jeg laget en __str__ til spilleliste, men innså for sent at dette kunne brukes i oppgaven til at det ble implementert på den måten.
                                #Siden dette var en valgfri del av oppgaven har jeg derfor unngått å implementere bruken av det.
                                #Jeg la derimot til en "print(allMusikk)" i slutten av spillelistetester.py for å se __str__ i bruk.
