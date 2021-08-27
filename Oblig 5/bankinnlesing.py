#Oppgave 5: Egen Oppgave

#Lag et program som lar deg ta inn en bankutskrift for å gi bruker om hvordan pengebruken har vært siden sist.
#Programmet skal la brukeren kategorisere bruken sin for å få en oversikt over hva pengene går til
#Vis bruker også hvor mye han har brukt totalt i måneden
#Skriv ut en ny fil som gir bruker en ryddig oversikt.

#Programmet definerer en funksjon som leser inn bankutskriften
def readFile(filename):
    file = open(filename, "r")
    dictionary = {}
    #Det opprettes et tomt bibliotek. For hver linje i filen som ble lest inn mates data fra filen inn i biblioteket.
    for lines in file:
        columns = lines.split(";")
        #Det kom med noen karakterer fra csv-filen min som jeg har fjernet - først ved å replace for expense
        expense = columns[0].replace(u'\ufeff','')
        #Og så ved å ikke ta med de to siste karakterene av pris. Om jeg ikke gjorde det fikk jeg meg "\n" for hver pris.
        price = float(columns[1][:len(columns[1])-2])
        #Hver utgift blir en nøkkel i ordboken, og prisene blir lagt til en liste for nøklene i ordboka
        if expense in dictionary:
            dictionary[expense].append(price)
        #For den første av hver utgift blir det lagt til en tom liste slik at programmet kan appende verdiene inn i listen.
        else:
            dictionary[expense] = []
            dictionary[expense].append(price)
    return dictionary

#Denne funksjonen lar brukere kategorisere de forskjellige utgiftene
def categorizeExpense(dictionary):
    categoryDict = {}
    print("Categorize your expenses, like 'Groceries'/'Business'/'Fun' etc.")
    #For hvert element i ordboken som blir tatt inn kan brukeren kategorisere det, som for eksempel at Rema1000 og Meny begge er 'matvarer'.
    for element in dictionary.keys():
        category = input("What do you categorize " + element + " as? ")
        if category in categoryDict:
            categoryDict[category].append(element)
        else:
            categoryDict[category] = []
            categoryDict[category].append(element)
    return categoryDict

#Denne funksjonen summerer opp de forskjellige utgiftene
def sumExpenses(dictionary1,dictionary2):
    summedDict = {}
    #For hvert element i ordbok nr 2, altså ordboken over de kategoriserte utgiftene, legges det til en verdi som skal summere opp totalprisen for den kategorien
    for key in dictionary2.keys():
        summedDict[key] = 0
        #For hvert element i den første ordboken, altså oversikten over alle kjøpene for hver utgift, summerer vi opp prisene slik at vi får totalsum på for eksempel kjøpene hos Meny.
        for element in dictionary1.keys():
            if element in dictionary2[key]:
                #Vi summerer en avrundet sum av elementene i den første ordboken og går så gjennom alle elementer for å få totalsummer.
                categorySum = round(sum(dictionary1[element]),2)
                summedDict[key] = summedDict[key]+categorySum
    return summedDict

#Den siste funksjonen tar inn den summerte ordboken og skriver ut informasjonen til en ny fil
def writeFile(dictionary,filename):
    file = open(filename, "w")
    #Vi lagrer totalsummen av alle kjøpene i en variabel
    totalExpense = sum(dictionary.values())
    file.write("Expenses overview: \n\n")
    #For hver av nøklene i ordboken skriver vi ut informasjon over hvor mye brukeren har brukt på denne kategorien, og hvor mye det er av totalkjøpet i en prosentandel.
    for keys in dictionary:
        file.write("%-10s %10s" % (keys+": ",str(dictionary[keys])+" - this is " + str(round((dictionary[keys]/totalExpense)*100,2))+ " % of your total expenses. \n"))
    file.write("\n")
    #Til slutt skriver vi ut hvor mye de totale utgiftene var.
    file.write("%-10s %10s" % ("Total expenses: ", str(totalExpense)))
    file.close()

#De 4 funksjonene kjøres til slutt slik at ordbøkene og filen blir opprettet.
dictionary=readFile("bankutskrift.csv")
categoryDict = categorizeExpense(dictionary)
summedDict = sumExpenses(dictionary,categoryDict)
writeFile(summedDict,"expenseoverview.txt")
