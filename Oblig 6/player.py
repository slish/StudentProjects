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

#Vi oppretter klassen spiller og tar inn to parameter fra bruker: navn og attributt.
#Baser på om spilleren velger å være smart, karismatisk eller business-smart får
#spilleren bonus i diverse valg.
class Player:
    def __init__(self, name, attribute):
        #Attributt-biblioteket inneholder bonusene som så blir satt til attributter
        #til Player. Noen valg blir så ganget med disse bonusene for å påvirke valget.
        attributeDict = {"Smart":[1.5,0.8,1], "Charismatic":[0.9,1.5,0.9], "Business":[0.8,1,1.5]}
        self._attribute = attribute
        self._smartness = attributeDict[self._attribute][0]
        self._charisma = attributeDict[self._attribute][1]
        self._business = attributeDict[self._attribute][2]
        self._name = name
        #Spilleren starter med penger, våkenhet, sult, forståelse, moro, tid og oppmøte.
        #Målet er å få forståelse så høyt som mulig, samtidig som man opprettholder sine
        #andre attributter.
        self._money = 1000 * self._business
        self._alertness = 100
        self._hunger = 50
        self._understanding = 0
        self._fun = 50
        self._time = 0
        self._attendance = 0

    #boringTask blir kalt på ofte for å minske spillerens trøtthet, moro og sult.
    def boringTask(self):
        self._fun -= 5
        self._alertness -= 20
        self._hunger -= 10

    #For å straffe spilleren for å skippe søvn og mat har jeg opprettet to funksjoner
    #som returnerer et tall som blir større jo mer mangel på søvn og mat spilleren har.
    #Dette blir så brukt til å trekke fra hvor mye man klarer å lære.
    def lackOfFood(self):
        lackOfFoodModifier = 0
        if self._hunger <= 20:
            lackofFoodModifier = (20-self._hunger)/5
        return lackOfFoodModifier

    def lackOfSleep(self):
        lackOfSleepModifier = (100-self._alertness)/20
        return lackOfSleepModifier

    #Diverse funksjoner blir kalt på når spilleren gjør ulike valg. Disse påvirker
    #attributtene til spilleren og printer ut en beskjed på hva som blir gjort.
    def lecture(self):
        self._understanding += 5.5*self._smartness-Player.lackOfSleep(self)-Player.lackOfFood(self)
        self._attendance += 1
        Player.boringTask(self)
        print("You go to the lecture for the week and feel that you understand this week's curriculum")

    def study(self):
        lackOfSleepModifier = (100-self._alertness)/20
        Player.boringTask(self)
        #Om spiller ikke har vært på forelesning får han en liten straff på hvor mye
        #det går an å lære på egen hånd.
        if self._attendance <= self._time:
            print("You study on your own, but having missed the lecture it's hard to really grasp some of the concepts.")
            print("You're not learning as much as you could have, but at least you're grasping all the concepts now.")
            self._understanding += (5.5*self._smartness)/2-Player.lackOfSleep(self)-Player.lackOfFood(self)
            self._attendance += 1
        else:
            print("You lean over your books, finding the concepts easy to understand after having seen them at the lecture.")
            self._understanding += 5.5*self._smartness-Player.lackOfSleep(self)-Player.lackOfFood(self)

    def play(self):
        print("You find some time to relax and play some games.")
        self._fun += 20
        self._alertness -= 20
        self._hunger -= 10

    def work(self):
        print("Time to get some cash. It might be boring, but sometimes it can't be helped.")
        Player.boringTask(self)
        self._money += 200*self._business

    def sleep(self):
        print("You take a well deserved rest in your bed and find yourself energized.")
        self._alertness = 100

    #def girlfriend(self):

    def orderFood(self):
        if self._money < 300:
            print("You can't afford to order food, so you eat the crusty leftovers in your fridge...")
            self._hunger += 20
        else:
            print("You spend 300 on some food that you eat in front of the TV. Your mind is soothed.")
            self._money -= 300
            self._hunger += 50
            self._fun += 10

    #Når en dag er over får spiller en liten oversikt over sine attributter.
    def timePass(self):
        self._time += 1
        self._understanding = round(self._understanding,2)
        print("Alertness: " + str(self._alertness) + ". Hunger: " + str(self._hunger) + ". Money: " + str(self._money) + ". Fun: " + str(self._fun) + ". Understanding: " + str(self._understanding))

    #playerChoice lar spiller foreta et valg på hva som skal skjer.
    #Lister og bibliotek blir brukt til å holde orden på forskjellige ting som skal skje,
    #og varselsbeskjeder når søvn-, sult- og moro-attributtene blir lave.
    def playerChoice(self):
        period = ["morning", "day", "night"]
        studyChoice = ["lecture", "study", "study"]
        sleepDict = {40: "You are starting to feel tired.", 20: "You are feeling quite tired, you might crash any minute", 0: "You collapse to the floor."}
        foodDict = {20: "You are starting to feel peckish.", 10: "Your stomach is growling.", 0: "With nothing in your stomach focusing becomes impossible. You better eat soon!"}
        funDict = {15: "You feel slightly bored.", 10: "The days seem to blend..", 5: "When was the last time you did something fun..?", 0: "Existensial dread sets in......"}
        #choiseDict er et bibliotek som inneholder funksjoner som kan bli kalt på.
        #På denne måten kan jeg lett kalle på funksjoner basert på hva spiller har trykket på.
        choiseDict = {"a": [Player.lecture,Player.study,Player.study], "b": Player.play, "c": Player.work, "d": Player.sleep, "e": Player.orderFood}
        for i in range(0,3):
            #Det blir kjørt noen sjekker på om spiller er før trøtt, sulten eller
            #kjeder seg for mye. Å nå null kan ha konsekvenser.
             if self._alertness in sleepDict:
                 print(sleepDict[self._alertness])
                 if self._alertness == 0:
                     print("You fall asleep where you stand until the next day")
                     self._alertness = 80
                     break
             if self._hunger in foodDict:
                 print(foodDict[self._hunger])
             if self._fun in funDict:
                 print(funDict[self._fun])
                 if self._fun == 0:
                     print("You have no will to do anything productive for the rest of the day. You stare at the wall, and find that highly entertaining compared to studying.")
                     self._fun = 20
                     break

             print("\nIt has become " + period[i] +". What do you do?")
             print("a) Go to " + studyChoice[i] +". b) Play some games. c) Work a shift")
             print("d) Sleep in your bed. e) Order food. ")
             activity = "Not chosen"
             while activity.lower() not in ["a","b","c","d","e"]:
                 activity = input()
                 if activity.lower() not in ["a","b","c","d","e"]:
                     print("Wrong input, choose betwen a,b,c,d or e.")
             print("\n" + "*" * 100)
             #Når spiller har valgt aktivitet henter vi fram funksjonen fra
             #tidligere bibliotek og legger til "(self)" for å kjøre dette
             #som en funksjon.
             if activity.lower() == "a":
                 choiseDict[activity][i](self)
             else:
                 choiseDict[activity](self)
             print("*" * 100)
             if self._hunger < 0:
                 self._hunger = 0
