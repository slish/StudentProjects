#Programmet definerer klassen Sang og alle funksjonene man kan kalle på for Sang-objekter

class Sang:
    def __init__(self,artist,tittel):
        self._tittel = tittel.lower().split() #Artist og tittel blir lagret som en ord-liste med små bokstaver for å enklere kunne iterere gjennom de senere
        self._artist = artist.lower().split()

    def spill(self):
        tittelStr = " ".join([
            word.capitalize()
            for word in self._tittel
            ])                          #Siden konstruktøren gjør om tittel og artist til lowercase bruker jeg en join-funksjon med capitalize for å få tittel og artist med store bokstaver
        artistStr = " ".join([
            word.capitalize()
            for word in self._artist
            ])
        print("Spiller " + tittelStr + " av artisten " + artistStr + ".")

    def sjekkArtist(self,navn):
        if isinstance(navn,list):   #Siden navn både kan være en liste og en vanlig streng (i min løsning av oppgaven) tar jeg en sjekk på om variabelen artistList kan legges inn direkte
            artistList = navn       #eller om jeg må konvertere strengen om til en liste først
        else:
            artistList = []
            for word in navn.split():
                artistList.append(word.lower())
        artistBool = False
        for artist in artistList:
            if artist in self._artist:
                artistBool = True
        return artistBool

    def sjekkTittel(self,tittel):
        if isinstance(tittel,list):
            titleList = tittel
        else:
            titleList = []
            for word in tittel.split():
                titleList.append(word.lower())
        titleBool = False
        for title in titleList:
            if title in self._tittel:
                titleBool = True
        return titleBool

    def sjekkArtistOgTittel(self,artist,tittel):
        if Sang.sjekkArtist(self,artist) and Sang.sjekkTittel(self,tittel):
            return True
        else:
            return False

    def __str__(self):
        tittelStr = " ".join([
            word.capitalize()
            for word in self._tittel
            ])
        artistStr = " ".join([
            word.capitalize()
            for word in self._artist
            ])
        return f"Sang: {tittelStr}\nArtist: {artistStr}"
