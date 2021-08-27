#Oppgave 4: Dato
'''
Filen inneholder klassen dato og alle dens instansvariabler og -metoder.
'''
class Dato:
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._dag = nyDag
        self._maaned = nyMaaned
        self._aar = nyttAar

    def hentAar(self):
        return self._aar

    def hentDag(self):
        return self._dag

    def datoStreng(self):
        return (str(self._dag) + "." + str(self._maaned) + "." + str(self._aar))

    def sjekkDato(self):
        if self._dag == 15:
            sjekkString = "Loenningsdag!"
        else:
            sjekkString = "Ingen loenningsdag i dag ..."
        if self._dag == 1:
            sjekkString = sjekkString + "\nNy maaned, nye muligheter"
        return sjekkString


#nyDato-funksjonen sjekker om datoen er før eller etter ved å anta at datoen som
#er skrevet inn er på formatet som oppgitt (ddmmyyyy). Da kan vi finne oppgitt
#dag, måned og år ved å ta ut deler av strengen som er oppgitt og konvertere det
#til en integer.
#Funksjonen forsøker først å finne de enkleste sjekkene der enten år eller måned
#er større eller mindre enn original dato, før den sjekker om dag er større eller
#mindre om det ikke er tilfelle. Om ingen av disse er tilfelle må datoen være
#den samme.


    def nyDato(self, dato):
        _etterDato = "Den nye datoen er etter original dato."
        _foerDato = "Den nye datoen er før original dato."
        _sammeDato = "Den nye datoen er samme dato som original dato."
        if int(dato[4:]) > self._aar:
            nyString = _etterDato
        elif int(dato[4:]) < self._aar:
            nyString = _foerDato
        else:
            if int(dato[2:4]) > self._maaned:
                nyString = _etterDato
            elif int(dato[2:4]) < self._maaned:
                nyString = _foerDato
            else:
                if int(dato[:2]) > self._dag:
                    nyString = _etterDato
                elif int(dato[:2]) < self._dag:
                    nyString = _foerDato
                else:
                    nyString = _sammeDato
        return nyString

#leggTilDag legger til en dag på datoen. Den kjører et par sjekker på datoen
#for å se om det må legges til en måned eller et år i tillegg til å måtte
#"resette" dagen til 1.
# - Første sjekk er om det er siste dag i året: måned og dag må da "resettes"
#   til 1, mens vi legger til 1 til år.
# - Andre sjekk ser etter om dagen er den siste dagen blant de korte månedene
#   (april, juni, september eller november) eller siste dag i de lange månedene
#   (øvrige bortsett fra februar). Dag må da "resettes" til 1 og måned øke med 1.
# - Tredje sjekk ser etter om året er et skuddår eller ikke (delelig på 4), og om
#   det er siste dag i februar basert på om det er skuddår eller ikke. Dag må da
#   "resettes" til 1 og måned øke med 1.
# - Om det ikke er noen av delene over legges det bare på en dag.
# - Det gjøres ingen sjekk på om bruker har lagt inn en "ugyldig" dag som
#   33.mai 2000. Jeg kunne ha gjort dette, men føler ikke det legger til noe
#   veldig ekstra til oppgaven og har derfor skippet det.

    def leggTilDag(self):
        kortMaanedSjekk = [4,6,9,11]
        if self._maaned == 12 and self._dag == 31:
            self._aar += 1
            self._maaned = 1
            self._dag = 1
        elif self._maaned in kortMaanedSjekk and self._dag == 30:
            self._dag = 1
            self._maaned += 1
        elif self._maaned not in kortMaanedSjekk and self._dag == 31:
            self._dag = 1
            self._maaned += 1
        elif self._aar % 4 == 0 and self._maaned == 2 and self._dag == 29:
                self._dag = 1
                self._maaned += 1
        elif self._aar % 4 != 0 and self._maaned == 2 and self._dag == 28:
                self._dag = 1
                self._maaned += 1
        else:
            self._dag += 1
