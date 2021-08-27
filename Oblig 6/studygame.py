#Oppgave 6: Egen oppgave
#Lag et spill om en student som må foreta valg før eksamen.
#Opprett en klasse som gir attributter til studenten og lag et hovedprogram
#som oppretter studenten som et objekt. La studenten gjøre ulike valg som
#påvirker karakteren han får til eksamen.

#KOMMENTAR:
#Det var i tidlig fase planlagt å ha med en kjærestekarakter som du også kunne
#tilbringe tid med. Dette skulle kunne gi deg bonuser om du tilbrakte nok tid med
#denne personen, men for å holde oppgaven innen et visst skop ble dette skrapet.
#Karisma-attributten er dermed et eksempel på noe som aldri blir brukt.
#Spiller har også sjelden behov for å jobbe for mer penger,
#så bonusen for å være business-savvy kommer ikke så godt med i spillet.
#Spillmessig trenger nok oppgaven en del jobb for å være et fullverdig spill,
#men ellers gjør funksjonene som de skal og jeg har ikke funnet noen bugs
#etter et par tester.

from player import Player

attributeDict = {"a": "Smart", "b": "Charismatic", "c": "Business"}
gradeDict = {89: "A", 77: "B", 65: "C", 53: "D", 41: "E", 0: "F"}

#Spiller får velge navn og om karakteren er smart, karismatisk eller business-savvy.
playerName = input("What is your name? ")
playerSelection = "Not selected"
while playerSelection.lower() not in ["a","b","c"]:
    playerSelection = input("Is your player: \na) Smart\nb) Charismatic\nc) Business-savvy\n")
    if playerSelection.lower() not in ["a","b","c"]:
        print("Wrong input. Please select a, b or c")
playerAttribute = attributeDict[playerSelection.lower()]
player = Player(playerName, playerAttribute)

exam = 7

for weeks in range(0,exam):
    player.playerChoice()
    player.timePass()

#Når spillet er over får man oppgitt hvilken karakter spilleren oppnådde på eksamen.
print("The day for the exam is here! After a lot of hard work you do your best. ")
for key in gradeDict:
    if player._understanding > key:
        grade = gradeDict[key]
        break
print("Your final grade is: " + grade)
