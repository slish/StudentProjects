#Oppgave 3: Billettpris

#Jeg lager en prosedyre der aldersverdien er 0. Dette er for å kunne kalle på prosedyren uten argumenter for så å spørre brukeren om hva alderen skal være.
def alderInput(ageValue = 0):
    if ageValue == 0:
        alder = int(input("Hva er din alder? "))
    else:
        alder = ageValue
    #Variabelen billettPris inneholder prisen på billetten. Det kjøres så en sjekk på alderen for å endre på billettprisen.
    billettPris = 0
    if alder <= 17:
        billettPris = 30
    elif alder > 17:
        billettPris = 50
    elif alder > 63:
        billettPris = 35
    #Prosedyren printer til slutt ut en beskjed med hva prisen på billetten er, basert på alderen som er oppgitt, enten av bruker eller av argumentet i prosedyren.
    print("Prisen på billetten din er:", billettPris, "kr.")

#Jeg kjører først prosedyren uten argument, det lar bruker skrive inn alder. Prosedyren kjører dermed med argumenter for å sjekke med alder 15, 31 og 63.
alderInput()
alderInput(15)
alderInput(31)
alderInput(63)

#Vi ser at det er noe galt med prosedyren siden personen på 63 år får samme billettpris som personen på 31 år. Dette er fordi vi først sjekker om personen er over 17 år, og
#siden 63 år er over 17 år blir denne sjekken sann. Vi kommer dermed aldri til sjekken om personen er 63 år eller eldre.
#For å korrigere prosedyren kunne vi i den andre if-setningen ha sjekket om personen var under 63 år, istedenfor å sjekke om personen er over 17 år.
