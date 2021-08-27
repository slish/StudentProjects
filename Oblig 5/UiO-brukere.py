#Oppgave 4: UiO-brukere

#Programmet oppretter et tomt bibliotek som skal inneholde UiO-brukerene
uioUsers = {}

#En ny funksjon blir opprettet for å lage brukernavn
def lagBrukernavn(name,dictionary):
    #Navnet som blir gitt som et argument blir splittet opp
    name = name.split()
    #Etternavnet blir satt til den første bokstaven i det andre elementet av navnet som ble gitt som et argument
    lastname = name[1][0]
    #Brukernavnet blir så satt til det fornavnet pluss den første bokstaven i etternavnet
    userName = name[0] + lastname
    existCheck = 0
    #Det kjøres en sjekk på om brukernavnet finnes fra før
    if userName.lower() in dictionary or userName in dictionary:
        #Vi kjører en løkke på lengen av etternavnet
        for i in name[1]:
            #Det lages et nytt brukernavn som inneholder en og en mer bokstav av etternavnet. Om etternavnet fortsatt finnes i ordboken etter en gjennomkjøring av løkka kjøres den en gang til,
            #helt til brukernavnet er unikt eller det ikke er flere bokstaver igjen i etternavnet som kan brukes.
            if userName in dictionary:
                existCheck += 1
                userName = name[0] + name[1][0:existCheck+1]
    return userName.lower()

#Programmet definerer en funksjon som setter sammen brukernavn med en alfakrøll og en suffix for å opprette en Epost.
def lagEpost(username,suffix):
    return username + "@" + suffix

#Programmet definerern en funksjon som går gjennom nøklene i ordboken som blir gitt som argument og printer epostene som blir lagd av brukernavn og suffiks i denne ordboken.
def printEposter(dictionary):
    for keys in dictionary:
        print(lagEpost(keys,dictionary[keys]))

#Programmet tester både første og andre funksjon for å se at resutatet er som forventet.
assert lagEpost(lagBrukernavn("Kari Nordmann",uioUsers),"student.matnat.uio.no") == "karin@student.matnat.uio.no"
printEposter({"olan": "ifi.uio.no2", "karian":"student.matnat.uio.no"})

#Vi setter userInput til en tom streng og kjører en while-løkke så lenge userInput ikke er "s"
userInput = ""
while userInput != "s":
    #Vi gir bruker et par kommandoer som kan brukes.
    userInput = input("Av(s)lutt/(P)rint ordbok/Skr(i)v inn bruker: ")
    #Vi har allerede sagt at løkken skal slutte om userInput ikke er "s", men ved å kjøre en sjekk på det her hindrer vi programmet fra å behøve å kjøre videre.
    if userInput.lower() == "s":
        break
    #Om bruker skriver inn "p" printer vi ut ordboken med brukere på UiO
    elif userInput.lower() == "p":
        printEposter(uioUsers)
    #Om bruker skriver inn "i" lar vi bruker skrive inn et navn og en suffix
    elif userInput.lower() == "i":
        name = input("Skriv inn navnet til brukeren: ")
        suffix = input("Vennligst skriv inn et suffix til brukeren din: ")
        userName = lagBrukernavn(name,uioUsers)
        uioUsers[userName] = suffix
    else:
        print("Kommando ikke gjenkjent. Vennligst prøv på nytt")
