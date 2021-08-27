#Oppgave 4: Matplan

foodDictionary = {"Kari Nordmann": ["Brød", "Egg", "Pølser"], "Ola Svenskmann": ["Polarbrød", "Kaker", "Pudding"], "Daniel Danskmann": ["Røde pølser", "Omelett", "Vafler"]}

def foodPlan():
    print("Beboerne på hjemmet er: ")
    for i in foodDictionary:
        print([i])
    chosenName = input("Hvilken beboer vil du sjekke matplanen til? ")
    if chosenName in foodDictionary:
        print("Matplanen til", chosenName, "består av:", foodDictionary[chosenName])
    else:
        print("Den beboeren er ikke i dette etablissementet.")

foodPlan()

#3a. Jeg ville ha brukt en liste for brukernavn for å få de i en rekkefølge. Da kan man lete opp et brukernavn og få et indeks i listen som man kan kalle på senere.
#   Om rekkefølgen ikke er så nøye ville jeg ha brukt en mengde. Siden brukernavnene er unike kan man bruke en mengde, og en mengde er litt mer effektiv å jobbe med.
#3b. For brukernavn og poeng ville jeg ha brukt en ordbok, slik at jeg kunne tildele poengene til brukeren som fikk poengene.
#3c. For alle vinnere kan et navn dukke opp flere ganger (hvis man er meget heldig kan man jo vinne flere ganger), så da ville jeg ha brukt en liste.
#3d. For all mat som noen er allergisk mot ville jeg ha brukt en liste siden en matrett kan dukke opp flere ganger.
