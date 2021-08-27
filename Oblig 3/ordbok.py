#Oppgave 2: Ordbok

#Det opprettes en ordbok som inneholder varer og prisene på disse. Denne blir printet til terminalen. 
myDictionary = {"Melk": 14.90, "Brød": 24.90, "Yoghurt": 12.90, "Pizza": 39.90}
print(myDictionary)

#Jeg lager en ny prosedyre som tar inn input fra brukeren på hva de vil selge og hva det skal koste. Prisen blir gjort om til en flyt-verdi.
#Varen og prisen som blir oppgitt blir så lagt til ordboken
def addWares():
    userWare = input("Hva vil du selge? ")
    userPrice = float(input("Hva skal det koste? (xx.xx) "))
    myDictionary[userWare] = userPrice

#Prosedyren kjøres to ganger slik at bruker får lagt til to ting
addWares()
addWares()

#Ordboken printes til terminalen
print(myDictionary)
