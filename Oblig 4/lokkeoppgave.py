#Oppgave 5: Egen Oppgave

#Lag et program som lar brukeren lage en nettbutikk der han får skrive inn hvilke varer som skal selges og til hvilken pris. La bruker også oppgi hvilke momssats
#som gjelder for de forskjellige varene og print ut en oversikt over hva brukeren skal selge og hva ting vil koste før og etter moms.

#Siden regnskapsførere gjerne opererer med momskoder oppretter jeg et bibliotek over momskodene og de tilhørende satsene
vatCode = {3:.25,31:.15,32:.12}

#Funksjonen wares kjører gjennom en forløkke et oppgitt antall ganger og lar bruker sette inn varer, pris og momskode
def wares(items):
    #Lister blir lagd for varer, pris og moms
    wares = []
    price = []
    vat = []
    #Waresdict skal være et bibliotek som inneholder varene, med tilhørende pris og momskode
    waresDict = {}
    #Forløkken kjører gjennom og fyller vare- , pris- og moms-listen.
    for i in range(0, items):
        wares.append(input("Hva er din " + str(i+1) + ". vare? "))
        price.append(float(input("Hva skal " + str(wares[i]).lower() + " koste? ")))
        vat.append(int(input("Hvilken momskode har denne varen? 3: 25%, 31: 15%, 32: 12% ")))
    #Når forløkken har kjørt ferdig putter jeg verdiene inn i et nøstet bibliotek.
    waresDict = dict(zip(wares, zip(price, vat)))
    return waresDict

#Bruker blir bedt om å oppgi antall varer som skal selges slik at vi kan bruke dette som et argument i funksjonen
numItems = int(input("Hvor mange varer skal du selge i butikken din? "))
#Forløkken i funksjonen kjører så mange ganger som bruker har oppgitt.
myDictionary = wares(numItems)
#Forløkken kjører gjennom hver nøkkel i biblioteket vi får ut fra funksjonen.
for i in myDictionary:
    #Valgt moms er det andre elementet i den tilhørende nøkkelen i biblioteket.
    vatSelected = myDictionary[i][1]
    #Vi finner tak i momsraten ved å søke på momskodenøkkelen. Vi gjør om dette til en int og ganger med 100 for å kunne presentere dette i %-format til brukeren.
    vatPercentage = int(vatCode[vatSelected]*100)
    #Prisen blir hentet fra det første elementet i listen inne i biblioteket.
    price = myDictionary[i][0]
    #Bruker får presentert hva han selger, prisen til varen, moms-prosenten til varen og hva totalprisen på varen blir etter moms.
    #Vi antar i dette tilfellet at prisen bruker skriver inn er før moms, men kunne også ha snudd om på matematikken for å oppgi moms om pris som ble skrevet var inkludert moms.
    print("Du selger ",i.lower(), " til ", price, " kr. Varen har ", vatPercentage, "% i moms som gir en totalpris på ", price+(price*(vatPercentage/100)), " kr. ", sep="")
