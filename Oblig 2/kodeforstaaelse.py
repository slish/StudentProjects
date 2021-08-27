#Oppgave 4: Kodeforståelse og feilsøking

#1. Dette er ikke lovlig kode da variabelen b tar inn verdien fra a som blir gjort om til en integer.
#Det forsøkes så å plusse sammen integeren som er i b med en string "Hei!".
#Her måtte man i tilfelle ha gjort om variabelen b til en string før man plusset på "Hei".

#2. Om bruker skriver inn noe som ikke er et heltall vil vi få en feil i variabelen b som gjør input fra bruker om til en integer.
#Det er heller ingenting som skjer med programmet om bruker skriver inn et tall som er 10 eller høyere.
#Det er ikke nødvendigvis problematisk, men bruker får heller ingen feedback på inputen sin. 

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
