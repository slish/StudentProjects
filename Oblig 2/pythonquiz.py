#Oppgave 5: Egen Oppgave
#Skriv et program som gir bruker repetisjonsspørsmål fra uke 1 i IN1000
#Inkluder minst 4 spørsmål og gi bruker poeng per spørsmål han får korrekt.
#Presenter poengene til brukeren på slutten av quizen.

#Programmet starter med å putte poeng og navn i variabler
points = 0
name = input("Hi and welcome to our quiz on week 1 in IN1000! What is your name? ")
#Jeg lager en prosedyre som jeg kan kalle på hver gang noen svarer noe som er uventet.
def wronganswer():
    print("I don't understand your answer, but it looks incorrect.")
    print("I'm afraid I can't give you any points for that.")

#Bruker blir gitt 4 spørsmål og for hvert korrekte spørsmål legger vi til et poeng
#Vi gir også en tilbakemelding på korrekt svar og på det som er forventet feil svar.
#Om bruker svarer noe annet enn det som er forventet for både korrekt og feil svar gir vi en tilbakemelding på at det ser feil ut.

#Question 1
question = input(name + " is a lovely name! On to the first question. Is print a function? (yes/no) ").lower()
if question == "yes":
    points += 1
    print("Good! Print is a function.\n")
elif question == "no":
    print("I'm afraid print is indeed a function.\n")
else:
    #Jeg prøvde først å definere første spørsmål i en prosedyre slik at jeg kunne kjøre spørsmålet om igjen om input fra bruker er utenom yes/no, men har ikke lært hvordan man får ut variabelen i prosedyren.
    wronganswer()

#Question 2
question = input('Second question. What would print("2" + "2") evaluate to? ')
#Vi kjører en liten ekstrasjekk på om bruker legger inn svaret som en streng med ""-tegnene. Siden dette er et lurespørsmål som returnerer en streng kan det tenkes at bruker vil skrive inn svaret i strengformat.
if question == "22" or question == '"22"':
    points += 1
    print("Great! Since the digits are in text format the print function adds them together as text.\n")
elif question == "4":
    print("It would make sense that 2+2=4, but since the digits are in text format the print function will add them together as text.\n")
else:
    wronganswer()

#Question 3
question = input("Third question: Can an integer contain decimals? (yes/no) ").lower()
if question == "no":
    points += 1
    print("Good! An integer has no fractional parts.\n")
elif question == "yes":
    print("Wrong, an integer has no fractional parts.\n")
else:
    wronganswer()

#Question 4
question = input("Fourth and final question: Can you have an if statement inside another if statement? (yes/no) ").lower()
if question == "yes":
    points += 1
    print("Great! If statements inside other if statements is usually called nested if statements.\n")
elif question == "no":
    print("You can actually have if statements inside other if statements, these are usually called nested if statements. \n")
    print()
else:
    wronganswer()

#Til slutt gir vi bruker en tilbakemelding basert på hvor mange poeng som ble oppnådd og presenterer antall poeng som ble oppnådd.
if points == 4:
    print("Great job, " + name + "! You got every question right! Your score is: " + str(points) + " out of 4 points.")
elif points > 1:
    print("Good job ," + name + ". You got most of the questions right, feel free to try again. Your score is: " + str(points) + " out of 4 points.")
else:
    print("Hmmmm, " + name + ". You didn't get many questions right, you might want to reread the chapters from week 1. Your score is: " + str(points) + " out of 4 points.")
