#Oppgave 1: Motorsykkel
'''
Programmet importerer klassen Motorsykkel og oppretter tre motorsykler i
hovedprogram(). Syklene får merke, registreringsnummer og kilometerstand,
og disse attributtene blir så skrevet ut til terminalen. Den tredje sykkelen
får seg en kjøretur på 10 km, og den nye kilometerstanden blir skrevet ut til
terminalen.
'''
from motorsykkel import Motorsykkel

def hovedprogram():
    sykkel1 = Motorsykkel("Ducati", "FN4126", 250)
    sykkel2 = Motorsykkel("Kawasaki", "NO1234", 500)
    sykkel3 = Motorsykkel("BMW", "LY4261", 350)
    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()
    sykkel3.kjor(10)
    print("Ny kilometerstand på sykkel3 er: " + str(sykkel3.hentKilometerstand()))

hovedprogram()
