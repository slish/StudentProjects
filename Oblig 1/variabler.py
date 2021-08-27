#Oppgave 1: Utskrift og innlesing med variabler
#I dette programmet etterspør vi et par navn fra bruker som blir returnert.
#Vi viser bruker også to konstanter som er lagret som variable, samt differansen av disse.

#Denne linjen etterspør input fra brukeren og lagrer det i variabelen 'name'
navn = input("Skriv inn navnet ditt her: ")
#Programmet utvides ved å legge til to variabler som inneholder heltall
helTall1 = 5
helTall2 = 9
#Variabelen differanse regner ut differansen mellom våre to heltallsvariabler.
#Ved å bruke den matematiske funksjonen abs() for å få det absolutte tallet av differansen sikrer
#jeg også at tallet som blir returnert er et positivt tall, uavhengig om helTall1 eller
#helTall2 blir endret til å være det største tallet.
differanse = abs(helTall1 - helTall2)
#Vi printer deretter teksten "Hei *navn*" ved å slå sammen tekst og variabelen 'name'
print("Hei " + navn)
#Etter velkomstbeskjeden printer vi de to heltallsvariablene
print(helTall1)
print(helTall2)
#Jeg printer ut teksten differanse og den faktiske differansen som vi lagret i en variabel tidligere
print("Differanse:", differanse)
#Bruker blir etterspurt å oppgi et nytt navn
navn2 = input("Oppgi et nytt navn: ")
#Denne variabelen legger sammen navnene som bruker har lagt inn
sammen = navn + navn2
print(sammen)
#Vi utvider programmet til å slå sammen navnene bruker har gitt, og legger et 'og' mellom navnene
sammen = navn + " og " + navn2
#Vi printer variabelen 'sammen' to ganger for å se på endringen av variabelen.
print(sammen)
