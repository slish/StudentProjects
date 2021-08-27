#Oppgave 1: Lister

#Vi lager først en liste med 3 tall og legger så til et tredje tall.
ownList = [9,27,81]
ownList.append(45)
#Det første og tredje tallet blir printet til terminalen.
print(ownList[0], ownList[2])

#En ny tom liste blir opprettet
yourList = []

#Vi lager en prosedyre for å hente inn et navn fra brukeren, og kaller så på denne prosedyren 4 ganger for å få 4 navn til listen
#Vi endrer inputen av navn til å være små bokstaver for at if-setningen senere ikke skal være case-sensitiv.
def enterName():
    yourList.append(input("Vennligst skriv inn et navn: ").lower())

for i in range(0,4):
    enterName()

#Navnet mitt blir lagt i en variabel, og det kjøres så en sjekk på om navnet mitt er inneholdt i den nye listen.
myName = "svein"
if myName in yourList:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#Vi lager nye variabler som først tar summen av den første listen ...
summedList = sum(ownList)
#og så tar produktet av den første listen ved hjelp av en loop.
productList = 0
for i in range(len(yourList)):
    if i > 0:
        productList = productList * ownList[i]
    #Når i = 0 endrer vi bare på variabelen istedenfor å multiplisere, for å unngå at noe ganget med 0 blir 0. Alternativt kunne vi initielt ha satt productList = 1.
    else:
        productList = ownList[i]

#Vi lager en ny liste som inneholder sum- og produkt-variablene.
mathList = [summedList, productList]
#Og lager enda en ny liste som slår sammen den første listen og sum/produkt-listen og skriver ut denne.
newList = ownList + mathList
print(newList)

#Vi fjerner deretter de to siste elementene ved å finne det siste elementet i lengden av listen to ganger. Deretter skriver vi ut listen på nytt.
newList.pop(len(newList)-1)
newList.pop(len(newList)-1)
print(newList)
