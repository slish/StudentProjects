#Oppgave 3: Hund

#Programmet importerer klassen Hund og lager en ny hund på 10 år og 10 kg(?).
#Hunden tar noen løperunder, kanskje løper den i en løkke, og tar av 2 kg i
#prosessen. Etter løpeturen har hunden to sesjoner med spising av rikelige
#porsjoner, og legger på seg det ene kiloet igjen.

from hund import Hund

def hovedProgram():
    myDog = Hund(10,10)
    for i in range(0,7):
        myDog.spring()
    print(myDog.hentVekt())
    myDog.spis(3)
    print(myDog.hentVekt())
    myDog.spis(3)
    print(myDog.hentVekt())

hovedProgram()
