#Oppgave 1: Utskriftsprosedyre
#Programmet etterspør en bruker om 3 forskjellige navn og plasser og returnerer en hilsen til hver av disse

#Vi putter koden som leser inn informasjon i en prosedyre
def information():
    name = input("Skriv inn navn: ")
    place = input("Hvor kommer du fra? ")
    print("Hei, " + name + "! Du er fra " + place + ".")

#Vi kaller på prosedyren 3 ganger for å få informasjon om 3 forskjellige personer
information()
information()
information()
