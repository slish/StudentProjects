#Oppgave 2: Konvertering
#Programmet konverterer en gitt temperatur fra fahrenheit til celsius.

#Vi etterspør en temperatur i fahrenheit fra brukeren og gjør dette om til float i tilfelle de etterspør en temperatur med desimaler
fahrenTemp = float(input("Oppgi en temperatur i fahrenheit (Bruk tall): "))
print("Fahrenheit:",fahrenTemp)

#Vi regner om dette til celsius ved å bruke fahrenheitverdien vi har fått og printer ut temperaturen i celsius.
#Celsiustemperaturen blir også avrundet til to desimaler. 
celsiusTemp = round(((fahrenTemp)-32) * 5 / 9,2)
print("Celsius:",celsiusTemp)
