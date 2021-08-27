#Oppgave 2: Regning med løkker

userInput = 1
inputList = []
#While-løkken kjører så lenge bruker ikke skriver inn '0'
while userInput != 0:
    userInput = int(input("Skriv inn et tall. Skriv 0 for å avslutte. "))
    #Så lenge bruker ikke skriver 0, blir tallet lagt til i listen inputList
    if userInput != 0:
        inputList.append(userInput)

#Forløkken går gjennom lengden til inputList og printer hvert element
for i in range(0,len(inputList)):
    print(inputList[i])

minSum =0
#Denne forløkken går gjennom hvert element i listen og legger det til i minSum
for i in range(0,len(inputList)):
    minSum += inputList[i]

minsteTall = 0
størsteTall = 0

for i in range(0, len(inputList)):
    #For det første elementet i listen legger vi verdien til minsteTall
    #For hvert element etter det første elementet sjekker vi om verdien til elementet er mindre enn minsteTall.
    #Om elementet er mindre endrer vi verdien, slik at vi alltid prøver å finne det minste elementet.
    if i > 0:
        if minsteTall>inputList[i]:
            minsteTall = inputList[i]
    else:
        minsteTall = inputList[i]

for i in range(0,len(inputList)):
    #For det første elementet i listen legger vi verdien til størsteTall
    #For hvert element etter det første elementet sjekker vi om verdien til elementet er større enn størsteTall.
    #Om elementet er større endrer vi verdien, slik at vi alltid prøver å finne det største elementet.
    if i > 0:
        if størsteTall<inputList[i]:
            størsteTall=inputList[i]
    else:
        størsteTall = inputList[i]

#Til slutt printer vi summen av tallene, det minste og det største tallet.
print("Summen av tallene du skrev inn er:",minSum)
print("Det minste av tallene du skrev inn var:", minsteTall)
print("Det største av tallene du skrev inn var:", størsteTall)
