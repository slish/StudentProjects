#Oppgave 3: Skop

#minFunksjon og hovedprogram blir først definert som funksjoner i programmet.
#Hovedprogramsfunksjonen blir kjørt der variablene a og b får tildelt variabler.
#b blir printet, og b har blitt tildelt verdien 0 som gjør at 0 blir printet til terminalen
#b blir tildelt variablen a. a var allerede tildelt verdien 42, så b er nå også tildelt verdien 42.
#a blir så tildelt returverdien av prosedyren minFunksjon, så koden hopper over i minFunksjon
#En forløkke kjører gjennom to ganger.
#Variabelen c blir tildelt verdien 2 og så printet. Det printer verdien 2.
#Variabelen c får verdien 1 addert, og har nå verdien 3.
#Variabelen b får verdien 10 tildelt.
#Variabelen b får variabelen a addert, men her vil programmet kræsje.
#Variabelen a er bare definert i en annen funksjon og er derfor lokal. Variabelen a er heller ikke definert globalt, og den er dermed ikke definert inne i prosedyren minFunksjon.

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()
