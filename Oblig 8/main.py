from spillebrett import Spillebrett
#Hovedprogrammet starter spillet Game of Life med en introduksjon og lar spillere velge mellom å spille spillet på normal måte eller
#se på noen av de forskjellige tilfellene som kan oppstå. Slik kunne jeg også teste at spillebrettet oppførte seg som forventet.

def main():
    print("*"*100)
    print("Velkommen til Game of Life!")
    print("Game of Life er et nullspiller-videospill/cellulaer automat som ble utviklet av John Horton Conway paa universitetet Cambridge i 1970.")
    print("Les mer om det paa wikipedia: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life")
    print("*"*100)
    gameChoice = ""
    options = [0,1,2,3,4,5,6,7]
    while gameChoice not in options:
        gameChoice = input("Hvilken spilletype vil du sette opp? Sett opp et normalt brett og se paa livet utfolde seg eller se paa noen av de spesielle tilfellene som kan oppstaa\n0 - Normalt brett\n1 - Block\n2 - Loaf\n3 - Blinker\n4 - Pulsar\n5 - Glider\n6 - Spaceship\n7 - Gosper glider gun\n")
        if intCheck(gameChoice) and int(gameChoice) in options:
            gameChoice = int(gameChoice)
        else:
            #Strengen i feilmelding er formatert til å se på det første og siste tallet i valg-listen, dermed blir denne stringen oppdatert om jeg skulle legge til flere valg.
            print("Vennligst velg mellom "+str(options[0])+"-"+str(options[-1])+"\n")
    normalGame(gameChoice)

#En del funksjoner vil ha heltall tilbake fra brukeren og jeg opprettet dermed en funksjon for å sjekke at det er det vi får tilbake
def intCheck(input):
    try:
        if isinstance(int(input),int):
            return True
    except:
        print("Vennligst skriv inn et heltall")
        return False

def normalGame(gameChoice):
    #Denne listen inneholder størrelsen på brettet avhengig av hvilken spilletype du har valgt
    boardSize = [[0,0],[4,4],[8,8],[5,5],[19,19],[20,20],[10,40],[30,50]]
    #I tilfelle det er det normale spillet tar vi inn input fra bruker om antall rader og kolonner
    if gameChoice == 0:
        rader = ""
        kolonner = ""
        choice = ""
        print("Vennligst sett opp spillebrettet.")
        while not isinstance(rader, int):
            rader = input("Hvor mange rader skal det vaere? ")
            if intCheck(rader):
                rader = int(rader)
        while not isinstance(kolonner,int):
            kolonner = input("Hvor mange kolonner skal det vaere? ")
            if intCheck(kolonner):
                kolonner = int(kolonner)
        boardSize[0][0] = rader
        boardSize[0][1] = kolonner
    rader = boardSize[gameChoice][0]
    kolonner = boardSize[gameChoice][1]
    choice = charChoice()
    gameBoard = Spillebrett(rader,kolonner,gameChoice)
    gameBoard.tegnBrett(choice)
    userInput = ""
    while userInput != "q":
        #Siden det er flere spilltyper er det lagt inn en funksjon for å starte nytt spill slik man fort kan sjekke ut de andre typene.
        userInput = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte. Skriv inn n og trykk enter for aa starte et nytt spill: ")
        if userInput == "":
            gameBoard.oppdatering()
            gameBoard.tegnBrett(choice)
        elif userInput == "n":
            main()
            #Loopen må breake ved nytt spill, ellers vil man komme tilbake til denne loopen etter et nytt spill. 
            break

#For å pynte litt på spillebrettet lot jeg brukeren velge hvordan cellene skal se ut på brettet
def charChoice():
    choice = ""
    options = [0,1,2,3,4]
    errMsg = "Vennligst velg mellom 0,1,2,3 eller 4\n"
    while choice not in options:
        choice = input("Hvilken karakter vil du spille som?\n0: ☺\n1: ♦\n2: §\n3: O\n4: Random\n")
        if intCheck(choice) and int(choice) in options:
            return int(choice)
        else:
            print(errMsg)
    return choice

main()
