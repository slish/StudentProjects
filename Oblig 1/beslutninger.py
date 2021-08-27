#Oppgave 2: Beslutninger
#I dette programmet spør vi bruker om han ønsker seg en brus og returnerer et svar basert på brukerens svar.

#Vi lagrer input fra brukeren i en variabel og endrer teksten som bruker har lagt inn til å være små bokstaver slik at
#if-setningen senere ikke vil være case-sensitiv.
brusValg = input("Kunne du tenke deg en forfriskende brus? (Ja/Nei) ").lower()
#Om brukeren svarer ja eller nei printer vi en tekst.
if brusValg == "ja":
    print("Her har du en brus!")
elif brusValg == "nei":
    print("Den er grei.")
#Om brukeren svarer alt annet enn ja eller nei gir vi en beskjed om at vi ikke forstår det som har blitt lagt inn.
else:
    print("Det forstod jeg ikke helt.")
