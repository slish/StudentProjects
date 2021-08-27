#Oppgave 4: Dato
'''
Programmet importerer klassen Dato og kjører tester på denne klassen.
Hovedprogrammet kjører noen metoder på datoen 15. mai 2000, mens
assertions-prosedyren kjører noen tester på metoden som legger til en dag,
og ser at stringverdien som blir returnert fra sjekkDato() ser ok ut når
det er den første i måneden. 
'''

from dato import Dato

def hovedProgram():
    minDato = Dato(15,5,2000)
    print("Året til datoen min er: " + str(minDato.hentAar()))
    print(minDato.sjekkDato())
    datoStreng = minDato.datoStreng()
    print("Datoen til programmet er: " + datoStreng)
    minDato.leggTilDag()
    datoStreng = minDato.datoStreng()
    print("Etter å ha lagt til en dag er datoen: " + datoStreng)

    nyDato = input("Skriv inn en ny dato: (ddmmyyyy) ")
    print(minDato.nyDato(nyDato))

def assertions():
    skuddAar = Dato(29,2,2000)
    ikkeSkuddAar = Dato(28,2,2001)
    kortMaaned = Dato(30,4,2000)
    langMaaned = Dato(31,5,2000)
    aarsSlutt = Dato(31,12,2000)
    datoListe = [skuddAar,ikkeSkuddAar,kortMaaned,langMaaned,aarsSlutt]
    for dato in datoListe:
        print("Før: " + dato.datoStreng())
        dato.leggTilDag()
        print("Etter: " + dato.datoStreng())
    print(aarsSlutt.sjekkDato())

hovedProgram()
assertions()
