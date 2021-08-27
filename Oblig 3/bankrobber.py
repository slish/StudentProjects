#Oppgave 5: Egen Oppgave

#Lag et spill hvor du er en skurk som skal ta med seg alle tingene i et hvelv.
#Bruk en ordbok for å angi hvilke objekter som er i rommet og hva som skjuler seg bak disse tingene.
#La brukeren få valget om å lete bak tingene, ta med seg skatter og forlate rommet.
#Gi bruker en vinnerbeskjed om han har funnet alle skattene når han forlater rommet.


import time
#Programmet lager et bibliotek over plasser brukeren kan lete, og hva som er inneholdt i de plassene
hidingSpots = {"Drawer": ["Gold watch", "Emerald"], "Safe": "Money", "Hatch": ["Diamond", "Stocks", "Diploma"]}
#Det lages så en tom liste som skal inneholde hva brukeren tar med seg
takenItems = []

print("You have entered the vault of the bank! Your goal is to get away with every item in the room before the police surrounds you.")

#Hva brukeren kan gjøre defineres i en prosedyre som senere blir kjørt flere ganger i en loop.
#Prosedyren returnerer en verdi som er falsk, dette er for å sjekke om loopen skal slutte å kjøre.
def userInput(exit = False):
    #To lister blir definert for å sjekke mot flere verdier som brukeren kan skrive inn
    lookAround = ["l", "look around"]
    exitVault = ["x", "exit", "exit the vault"]
    #Programmet plusser på en til en variabel som heter timer hver gang loopen kjøres. Dette fører til at brukeren kan tape om det blir skrevet for mange kommandoer.
    if timer >= 11:
        print()
        print("*"*60)
        print("You took too long! The police have surrounded you!")
        print("*"*60)
        time.sleep(5)
        #Om timeren går ut slutter loopen å kjøre.
        exit = True
    else:
        #Om timeren ikke har gått ut spør prosedyren om hva brukeren ønsker å gjøre. Brukeren får nøkkel-bokstaver som han kan skrive inn for å utføre ulike ting.
        print()
        action = input("What do you want to do? (l: look around) (x: exit the vault) ('object': check said object) ('item': take said item) ")
        print()
        #Om det brukeren skriver inn er i listen lookAround, får brukeren oppgitt en liste over objekter han kan lete i.
        if action in lookAround:
            print("You see the following objects in the room: ")
            for i in hidingSpots:
                print([i])
        #Om det brukeren skriver inn er inneholdt i biblioteket over ting han kan lete i, får han ut den tilhørende verdien til objektet.
        elif action in hidingSpots:
            print("The", action, "contains:", hidingSpots[action])
        #Om brukeren skriver inn det som er inneholdt i objektet, får han beskjed om at han nå har tatt skatten.
        elif any(action in val for val in hidingSpots.values()):
            #Om brukeren allerede har tatt en skatt kan den ikke tas om igjen. Bruker får da beskjed om at skatten allerede er tatt.
            if action in takenItems:
                print("You've already taken the", action)
            else:
                print("You take the", action, ".")
                #Skatten som er tatt blir lagt til i listen over skatter som er tatt
                takenItems.append(action)
        #Om det bruker skriver inn er inneholdt i listen exitVault, får brukeren oppgitt en beskjed basert på hvor mange ting som er tatt.
        elif action in exitVault:
            #Om bruker har tatt alle 6 skattene har han vunnet
            if len(takenItems) == 6:
                print("You've successfully escaped with all the items! Good job!")
            #Om bruker ikke har tatt en eneste skatt er det kanskje en hederlig person.
            elif len(takenItems) == 0:
                print("You've successfully escaped with no items. Maybe you are an honest person after all.")
            #Bruker får ellers beskjed over hvilke skatter som er tatt.
            else:
                print("You escape the vault and have taken with you the following items: ")
                print(takenItems)
            #Om bruker går ut av hvelvet slutter loopen å kjøre.
            time.sleep(5)
            exit = True
        #Om det bruker skriver inn ikke er blant noen av kommandoene får han en beskjed om at kommandoen ikke er forstått.
        else:
            print("I didn't quite understand that. Please try again")
    #Prosedyren returnerer verdien til exit, som blir True når bruker stikker av eller timer går ut. Det vil si at selve prosedyren returnerer True i dette tilfellet.
    return exit

#exitLoop bestemmer om loopen skal slutte å kjøre
exitLoop = False
#Timer er en variabel som starter på 0. Når denne når 11 blir bruker tatt av politiet.
timer = 0

#Denne loopen kjører helt til timeren når 11 eller bruker skriver inn "x", da vil prosedyren returnere True, som gjør at exit også blir True.
while exitLoop == False:
    if userInput() == True:
        exitLoop = True
    timer += 1
