#Oppgave 1: Regnefunksjoner


#Programmet definerer først 3 funksjoner som adderer, subtraherer og dividerer tall den får inn som argument
def addisjon(helTall1, helTall2):
    return helTall1 + helTall2

def subtraksjon(helTall1, helTall2):
    return helTall1 - helTall2

def divisjon(helTall1, helTall2):
    return helTall1 / helTall2

#Vi printer returverdien til addisjonsfunksjonen med argumentene 10 og 20, dette blir 30.
print(addisjon(10,20))

#Vi tester forskjellige verdier til funksjonene for å se at alt fungerer som tiltenkt.
assert addisjon(5,6) == 11
assert addisjon(-1,-2) == -3
assert addisjon(5,-5) == 0
assert subtraksjon(5,6) == -1
assert subtraksjon(-1,-2) == 1
assert subtraksjon(5,-5) == 10
assert divisjon(25,5) == 5
assert divisjon(-4,-2) == 2
assert divisjon(5,-5) == -1

#En funksjon for konvertering fra tommer til CM blir definert. Det blir kontrollert at argumentet er større enn 0 før argumentet blir multiplisert med 2,54
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

assert tommerTilCm(1) == 2.54

#Den siste funksjonen i programmet tar i bruk brukerinput og tidligere funksjoner som har blitt definert
def skrivBeregninger():
    print("Utregninger:")
    #To tall blir hentet inn fra bruker
    brukerTall1 = float(input("Skriv inn tall 1: "))
    brukerTall2 = float(input("Skriv inn tall 2: "))
    print()
    #Tall fra bruker blir brukt som argument i tidligere definerte funksjoner
    print("Resultat av summering: " + str(addisjon(brukerTall1,brukerTall2)))
    print("Resultat av subtraksjon: " + str(subtraksjon(brukerTall1,brukerTall2)))
    print("Resultat av divisjon: " + str(divisjon(brukerTall1,brukerTall2)))
    print()
    print("Konvertering fra tommer til cm:")
    #Et nytt tall fra bruker blir hentet inn og brukt som argument i tommerTilCm-funksjonen
    tommerTall = float(input("Skriv inn et tall: "))
    print("Resultat: " + str(tommerTilCm(tommerTall)))

#Til slutt kaller vi på den siste funksjonen for at den faktisk skal kjøre når programmet kjøres.
skrivBeregninger()
