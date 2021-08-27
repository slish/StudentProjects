#Oppgave 1: Parametere og returverdier

#Funksjonen adder tar inn to heltall og returnerer summen av disse
def adder(helTall1, helTall2):
    return helTall1 + helTall2

#Programmet printer ut hva som blir returnert når tall blir lagt til som argumenter i funksjonen
print("Funksjonen min returnerer først:", adder(5,10))
print("Funksjonen min returnerer så:", adder(15,20))

#Bruker blir spurt om å legge inn en tekststreng etterfulgt av et mellomrom og en bokstav til slutt.
userInput = input("Skriv inn en tekststreng etterfulgt av en bokstav. ")

#Funksjonen tellForekomst tar inn en tekst og en bokstav som argument
def tellForekomst(minTekst,minBokstav):
    sumBokstav = 0
    #Forløkken kjører gjennom lengen av teksten minus den siste bokstaven for å ikke telle bokstaven en ekstra gange
    for i in range(0,len(minTekst)-1):
        if minTekst[i] == minBokstav:
            #Hver gang vi finner bokstaven i setningen legger vi til 1 i sumBokstav
            sumBokstav += 1
    return sumBokstav #sumBokstav blir returnert i funksjonen.

#Vi printer ut hvor mange ganger bokstaven som ble lagt inn forekommer i setningen.
print("Bokstaven", userInput[-1], "forekom", tellForekomst(userInput,userInput[-1]), "ganger i setningen din.")
