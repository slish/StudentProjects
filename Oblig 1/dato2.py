#Oppgave 3: Problemløsning med beslutninger

#Til å starte med ber vi brukeren legge inn to datoer.
#Vi ber bruker om å legge inn med et format på 4 siffer slik at vi kan hente ut det vi trenger
print("Tenk på en dato")
dato0 = input("Vennligst skriv inn datoen du tenkte på: (ddmm) ")
#De to følgende variablene tar de to første og de to siste tallene i det som ble lagt inn av bruker for å skille mellom dag og måned
dato0Dag = dato0[:2]
dato0Måned = dato0[2:]
print("Tenk på en ny dato")
dato1 = input("Vennligst skriv inn datoen du tenkte på: (ddmm) ")
dato1Dag = dato1[:2]
dato1Måned = dato1[2:]

#Vi lagrer svarene som kan bli returnert til brukeren i variabler slik at disse enkelt kan endres på et senere tidspunkt
feilFormat = "Du har skrevet inn feil format på en av datoene, bruk fire siffer for hvert svar - vennligst prøv igjen"
sameDato = "Samme dato!"
korrDato = "Riktig rekkefølge!"
errDato = "Feil rekkefølge!"

#Når brukeren har lagt inn datoene kjører vi først en sjekk på om svarene ikke inneholder 8 siffer tilsammen (4 + 4 siffer) og returnerer en feilmelding om dette er tilfelle.
if len(dato0+dato1) != 8:
    print(feilFormat)
#Om formatet er korrekt på alle datoene sjekker vi først om begge datoene er like og returnerer variabelen sameDato som gir oss teksten vi ønsker å gi til bruker.
elif dato0 == dato1:
    print(sameDato)
#For å se hvilken dato som kommer først sjekker vi først om samme måned er lagt inn. Om månedene er like må vi se hvilken dag som er først.
elif dato0Måned == dato1Måned:
    #Hvis samme måned er lagt inn sjekker vi hvilken dag som er først og returnerer enten riktig rekkefølge om den første dagen er først, og vice versa.
    if dato0Dag < dato1Dag:
        print(korrDato)
    else:
        print(errDato)
#Om månedene ikke er like trenger vi ikke å sjekke hvilken dag som er først, så til slutt ser vi etter hvilken måned som kom først og returnerer et svar basert på dette.
elif dato0Måned < dato1Måned:
    print(korrDato)
#Om dato0Måned ikke er lik dato1Måned (som vi sjekket tidligere) og ikke er mindre enn dato1Måned er det bare en mulighet igjen: At dato0Måned er større enn dato1Måned. 
#Vi trenger dermed ikke å sjekke om dato0Måned er større enn dato1Måned, og forenkler den siste setningen med å bare skrive else
else:
    print(errDato)
