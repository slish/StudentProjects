#Oppgave 4: Å telle bokstaver og ord

#Funksjonen myWord returnerer lengden av ordet som blir gitt til funksjonen.
def wordReturn(myWord):
    return len(myWord)

#Funksjonen mySentence returnerer et bibliotek med unike ord og hvor mange ganger de forekommer
def sentDictionary(mySentence):
    #Først splittes setningen i argumentet for å få en liste over ord
    sentList = mySentence.split()
    #Det lages en liste over unike ord og ordteller for å kunne mate lister inn i biblioteket
    uniqueWords = []
    wordCount = []
    #En forløkke kjører gjennom listen av ord i setningen, og om ordet ikke allerede er i listen blir det lagt til
    for i in range(0,len(sentList)):
        if sentList[i] in uniqueWords:
            pass
        else:
            uniqueWords.append(sentList[i])
    #En forløkke kjører gjennom den nye listen med unike ord
    for i in range(0,len(uniqueWords)):
        #For hvert ord i listen med unike ord ser programmet om det unike ordet er likt ordet i listen over ord i setningen som ble brukt som argument
        wordCounter = 0
        for j in range(0,len(sentList)):
            if uniqueWords[i] == sentList[j]:
                #Om ordet er likt legger vi til +1 til variabelen wordCounter
                wordCounter += 1
        #Hver gang den innerste forløkken har kjørt gjennom for et unikt ord legger vi til tallet i listen over ordtellingen
        wordCount.append(wordCounter)
    #Når jeg har fått laget to lister, en for unike ord og en for forekomster, lager jeg et bibliotek over disse to listene
    uniqueDict = dict(zip(uniqueWords, wordCount))
    #Biblioteket blir returnert
    return uniqueDict

#Programmet ber bruker skrive inn en setning og kjører funksjonen over på setningen.
userInput = input("Skriv inn en setning. ")
#Biblioteket som blir returnert blir lagret i variabelen myDictionary
myDictionary = sentDictionary(userInput)
#Programmet summerer opp forekomsten av ord i biblioteket for å få antall ord i setningen
print("Det er", sum(myDictionary.values()), "ord i setningen din. ")
#En forløkke kjører gjennom biblioteket og printer ut nøklene og verdien til setningen for å gi bruker informasjon over
#ordene og forekomster, og bruker så den første funksjonen for å også informere om antall bokstaver i ordene.
for i in myDictionary:
    #Vi kjører en sjekk på om ord forekommer 1 gang eller har 1 bokstav, for å endre på gramatikken som blir returnert.
    if myDictionary[i]==1:
        times = "gang"
    else:
        times = "ganger"
    if wordReturn(i) ==1:
        letters = "bokstav."
    else:
        letters = "bokstaver."
    print("Ordet '", i, "' forekommer ", myDictionary[i]," ", times, " og har ", wordReturn(i)," ", letters, sep="")
