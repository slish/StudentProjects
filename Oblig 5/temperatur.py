#Oppgave 2: Temperatur

#Programmet definerer en funksjon som tar inn et filnavn som argument
def readFile(filnavn):
    #Filen blir åpnet og et tomt bibliotek blir opprettet
    file = open(filnavn)
    dictionary = {}
    #For hver linje i filen tildeler vi verdiene som er skilt med et komma til variabler
    for lines in file:
        column = lines.split(",")
        month = column[0]
        temp = float(column[1])
        #Vi putter variablene inn i biblioteket vårt, og returnerer så dette biblioteket.
        dictionary[month] = temp
    return dictionary

#Et nytt bibliotek blir opprettet som henter innholdet sitt fra funksjonen over.
fileDictionary = readFile("max_temperatures_per_month.csv")
#Biblioteket blir printet.
print(fileDictionary)

#Det defineres så en ny funksjon som tar inn et bibliotek og et filnavn som argumenter
def readFile2(dictionary,filnavn):
    #Filen i argumentet åpnes
    file = open(filnavn)
    #Som i forrige funksjon kjører vi gjennom hver fil og tildeler verdier til variabler
    #Siden den andre filen har to komma'er tildeles verdiene nå til tre variabler istedenfor to
    for lines in file:
        column = lines.split(",")
        month = column[0]
        day = column[1]
        temp = float(column[2])
        #Om temperaturene i den nye filen er større enn verdien vi fant i tilsvarende måned i biblioteket printes det en beskjed, og biblioteket oppdateres
        if temp > dictionary[month]:
            print("Ny varmerekord på " + day +" "+ month + ": " + str(temp) + " grader Celcius. (gammel varmerekord var " + str(dictionary[month]) + " grader Celcius)")
            dictionary[month] = temp
    #Det oppdaterte biblioteket blir returnert
    return dictionary

#Vi oppdaterer biblioteket vi opprettet med det oppdaterte biblioteket vi fikk ut av funksjonen over
fileDictionary = readFile2(fileDictionary,"max_daily_temperature_2018.csv")
#Det oppdaterte biblioteket blir printet ut slik at vi lett kan se at verdiene faktisk har blitt oppdatert.
print(fileDictionary)

#En ny funksjon blir opprettet som tar et bibliotek og et filnavn som argument.
#Det nye her er at filnavnet i argumentet ikke trenger å være en eksisterende fil, man kan skrive inn et hvilket som helst filnavn for å opprette en ny fil
def writeFile(dictionary,filnavn):
    writtenFile = open(filnavn, "w")
    #For hver nøkkel i biblioteket vi tar inn skriver vi inn verdiene fra biblioteket til den nye filen.
    for keys in dictionary:
        writtenFile.write(keys+","+str(dictionary[keys])+"\n")

#Vi kjører til slutt funksjonen for å opprette en ny fil som inneholder biblioteket i korrekt csv-format.
writeFile(fileDictionary,"written_file.csv")

#Programmet definerer en funksjon som tar et filnavn som argument
def heatWaves(filnavn):
    file = open(filnavn)
    #Vi oppretter en variabel period som skal telle dager en varmebølge har vart
    period = 0
    for lines in file:
        column = lines.split(",")
        month = column[0]
        day = column[1]
        temp = float(column[2])
        if temp > 25:
            #Om temperaturen er over 25 grader og period er lik 0 (Det er den første dagen av en varmebølge), lagrer vi måned og dag for senere å kunne
            #hente tilbake starten på varmeperioden
            if period == 0:
                heatStart = day + ". " + month
            #Så lenge temperaturen er over 25 dager legger vi til 1 i periodetelleren
            period+= 1
            #Hver dato blir også lagt til som en slutt på varmebølgen. Denne blir oppdatert til vi ikke lenger har en dag som er over 25 varmegrader.
            heatEnd = day + ". " + month
        #Når vi når en dag som er under 25 varmegrader og periodetelleren er større eller lik 5 betyr det at vi har nådd slutten på en varmebølge
        #Vi printer da ut når bølgen startet, som vi lagret tidligere, og når bølgen endte, som var den siste dagen temperaturen var over 25 grader.
        #Vi printer også ut periodetelleren for å se på hvor lenge varmebølgen varte.
        if temp <= 25 and period >= 5:
            print("En hetebølge startet " + heatStart + " og sluttet " + heatEnd + ". Den varte i " + str(period) + " dager.")
            period = 0
        #Vi må også ha en sjekk på at temperaturen er under 25 og periodetelleren ikke har nådd 5. Da må vi resette periodetelleren.
        elif temp <= 25 and period < 5:
            period = 0

heatWaves("max_daily_temperature_2018.csv")
