#Oppgave 3: Reiseplan

#Jeg lager en funksjon som tar inn et antall for å si hvor mange ganger forløkken skal kjøre,
#og et argument for å angi hva brukeren skal skrive inn
def listInput(times, wish):
    liste = []
    #Funksjonen lager en liste som blir kjørt gjennom så mange ganger som argumentet times
    for i in range(0,times):
        #For hver iterasjon av løkken blir bruker spurt om å oppgi en ny ting, basert på argumentet wish
        liste.append(input("Oppgi 1 " + wish + ". "))
    return liste

#Programmet lager tre lister for steder, klesplagg og avreisedatoer. Funksjonen listInput blir så kjørt for å
#gi verdier til disse listene.
steder = []
klesPlagg = []
avreiseDatoer = []
steder = listInput(5,"sted")
klesPlagg = listInput(5,"klesplagg")
avreiseDatoer = listInput(5,"avreisedato")

#Programmet lager en ny liste reiseplan og legger til de forrige listene slik at vi har en nøstet samling
reiseplan=[]
reiseplan.append(steder)
reiseplan.append(klesPlagg)
reiseplan.append(avreiseDatoer)

#En forløkke printer ut alle verdiene i den nye nøstede samlingen
for i in range(0,len(reiseplan)):
    print(reiseplan[i])

#To nye variabler blir opprettet for å kunne velge liste og indeks i listen.
#Variablene blir satt til -1 initielt for å kunne starte løkken i funksjonen som kommer.
i1 = -1
i2 = -1

#Jeg oppretter en funksjon som tar en liste, en variabel og string som argumenter.
#Funksjonen spør bruker om hvilken liste eller element han vil se på, og kjører en sjekk på at det som blir svart er innenfor
#lengden til listen i argumentet.
#Bruker blir spurt om å oppgi et tall mellom 1 og lengden til listen for at det skal gi  mening for brukeren,
#så trekker vi fra 1 fra det som blir lagt inn for at tallet skal gi en mening for indeksen.
#Om bruker for eksempel vil se på den første listen skrives 1 inn, så trekker vi fra 1 for å få 0,
#som er den første indeksen.
def checkList(reiseListe, variabel, listOrElm):
    while variabel < 0 or variabel > len(reiseListe)-1:
        variabel = int(input("Hvilken "+listOrElm+ " vil du se på? Velg mellom 1 og " + str(len(reiseListe))+ ": "))-1
        if variabel < 0 or variabel > len(reiseListe)-1:
            print("Ugyldig input! Vennligst velg mellom 1 og " + str(len(reiseListe)))
    return variabel

#Funksjonen blir kjørt to ganger for å først la bruker velge blant reiseplanen, og så blant elementet til reiseplanslisten som ble valgt.
i1 = checkList(reiseplan,i1,"liste")
i2 = checkList(reiseplan[i1],i2,"element")

#Programmet printer ut hva som er inneholdt i valgt element i valgt liste.
print("Det ", i2+1, ". elementet i den ", i1+1, ". listen er: " , reiseplan[i1][i2], sep="")
