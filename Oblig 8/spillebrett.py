from random import randint
from celle import Celle

#Spillebrettklassen inneholder selve spillebrettet og metoder for å tegne/generere dette, hente ut status om antall levende celler og metode for å finne naboene til cellene.

class Spillebrett:
    def __init__(self,rader,kolonner,gametype):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []

        for y in range(0,self._rader):
            self._rutenett.append([])
            for x in range(0,self._kolonner):
                celle = Celle()
                self._rutenett[y].append(celle)
        self._generasjonsNr = 0
        Spillebrett._generer(self,gametype)
        #En liten forklaring blir gitt til spiller basert på spilletype som blir startet.
        forklaringsListe = ["Game of Life",
                            "Block er et ekstremt kjent og vanlig 'still life' som ble funnet av John Conway i 1970.",
                            "Loaf er et 7-cellers 'still life' oppdaget av JHC-gruppen i 1970.",
                            "Blinker er den minste og vanligste oscillatoren, funnet av John Conway i mars 1970.",
                            "Pulsar (sjelden referert til som Cambridge pulsar CP 48-56-72) er en stor, men overraskende vanlig period-3-oscillator. Den ble funnet av John Conway i mars 1970.",
                            "Glider (eller 'fjaervekt romskip') er det minste, vanligste og foerst oppdagede romskipet.",
                            "Et romskip (ogsaa referert til som en 'glider' eller sjeldnere en 'fisk', og ofte forkortet til 'skip') er et endelig moenster som gaar tilbake til sin opprinnelige tilstand etter flere generasjoner (kjent som sin periode) men paa et annet sted.",
                            "Gosper glider gun er den foerste kjente pistolen, og faktisk det foerste kjente endelige moensteret med ubegrenset vekst, funnet av Bill Gosper i november 1970."]
        self._text = forklaringsListe[gametype]


    def tegnBrett(self, choice):
        signs = []
        x = -1
        for list in self._rutenett:
            signs.append([])
            x += 1
            for cell in list:
                signs[x].append(cell.hentStatusTegn(choice))
        print("\n" *50)
        #Cellene blir satt sammen med en join-funksjon der jeg har brukt et mellomrom for å få spillebrettet litt mer kvadratisk.
        for list in signs:
            print(' '.join(list))
        print("Generasjon: " + str(self._generasjonsNr) + " - Antall levende celler: " + str(self.finnAntallLevende()))
        print(self._text+"\n")

    def oppdatering(self):
        deadCells = []
        liveCells = []

        for liste in self._rutenett:
            for cell in liste:
                #Her sjekkes antall levende/døde celler rundt en hver celle og status for cellen settes basert på dette ihht spillereglene
                liveCounter = 0
                for neighbor in self.finnNabo(self._rutenett.index(liste),liste.index(cell)):
                    if neighbor.erLevende():
                        liveCounter += 1
                if cell.erLevende():
                    if liveCounter < 2 or liveCounter > 3:
                        deadCells.append(cell)
                    else:
                        liveCells.append(cell)
                if not cell.erLevende():
                    if liveCounter == 3:
                        liveCells.append(cell)
                    else:
                        deadCells.append(cell)
        #For at ikke cellene skal skifte status mens sjekken pågår settes dette etterpå. Om cellene endret status i det vi gikk gjennom dem ville det ha ført til andre resultater.
        for cells in deadCells:
            cells.settDoed()
        for cells in liveCells:
            cells.settLevende()
        self._generasjonsNr += 1

    def finnAntallLevende(self):
        livingCells = 0
        for list in self._rutenett:
            for cell in list:
                if cell.erLevende():
                    livingCells+= 1
        return livingCells

    def _generer(self,gametype):
        #Denne listen inneholder koordinatene som trengs for å lage noen av de forskjellige tilstandene man kan komme ut for i Game of Life.
        #Block, Loaf, Blinker, Pulsar, Glider, Spaceship og Gosper glider gun
        #I tilfelle spiller velger '0' startes et normalt spill der cellene blir tilfeldig vekket til live, derfor er den listen tom.
        figurKoordinater = [[],
                            [(1,1),(2,1),(1,2),(2,2)],                                                  #Block
                            [(2,3),(2,4),(3,2),(3,5),(4,3),(4,5),(5,4)],                                #Loaf
                            [(2,2),(3,2),(4,2)],                                                        #Blinker
                            [(2,6),(2,12),(3,6),(3,12),(4,6),(4,7),(4,11),(4,12),(6,2),(6,3),(6,4),     #Pulsar
                                (6,7),(6,8),(6,10),(6,11),(6,14),(6,15),(6,16),(7,4),(7,6),(7,8),       # |
                                (7,10),(7,12),(7,14),(8,6),(8,7),(8,11),(8,12),(10,6),(10,7),           # |
                                (10,11),(10,12),(11,4),(11,6),(11,8),(11,10),(11,12),(11,14),           # |
                                (12,2),(12,3),(12,4),(12,7),(12,8),(12,10),(12,11),(12,14),(12,15),     # |
                                (12,16),(14,6),(14,7),(14,11),(14,12),(15,6),(15,12),(16,6),(16,12)],   #Pulsar
                            [(1,2),(2,3),(3,1),(3,2),(3,3)],                                            #Glider
                            [(3,1),(3,4),(4,5),(5,1),(5,5),(6,2),(6,3),(6,4),(6,5)],                    #Spaceship
                            [(2,26),(3,24),(3,26),(4,14),(4,15),(4,22),(4,23),(4,36),(4,37),(5,13),     #Gosper glider gun
                                (5,17),(5,22),(5,23),(5,36),(5,37),(6,2),(6,3),(6,12),(6,18),(6,22),    # |
                                (6,23),(7,2),(7,3),(7,12),(7,16),(7,18),(7,19),(7,24),(7,26),(8,12),    # |
                                (8,18),(8,26),(9,13),(9,17),(10,14),(10,15)]                            #Gosper glider gun
                            ]
        if gametype == 0:
            for list in self._rutenett:
                for cell in list:
                    if randint(0,2) == 2:
                        cell.settLevende()
        else:
            Spillebrett._customGenerator(self,figurKoordinater[gametype])

    def _customGenerator(self,cellList):
        x = -1
        #For spill med fastsatte figurer henter vi koordinater og vekker til live de cellene som har x,y-tupler i koordinatlisten.
        for list in self._rutenett:
            x +=1
            y = -1
            for cell in list:
                y += 1
                if (x,y) in cellList:
                    cell.settLevende()

    #finnNabo-funksjonen finner alle nabocellene til den nåværende listen og returnerer en liste over naboene.
    def finnNabo(self,rad,kolonne):
        naboList = []
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    pass
                else:
                    if kolonne+j < 0 or kolonne+j > self._kolonner-1:
                        pass
                    elif rad+i < 0 or rad+i > self._rader-1:
                        pass
                    else:
                        naboList.append(self._rutenett[rad+i][kolonne+j])
        return naboList
