"""Jeg begynte først å lage et diagram om hvordan programmet/Kalkulatoren skulle oppføre seg. Så begynte jeg med databasen. Så laga jeg en loop med minst to tall 
og et tegn, og med 'if' for å gi bruker mulighet til å legge sammen fler tall. Så var det selve kalkulatoren og da kom jeg fram til at if var en fin løsning.
og alt dette legges til slutt i databasen."""


#tilkobling til databasen
#Jeg tenke jeg må legge login informasjonen i en annen seperat kode. for at hackere ikke kommer inn i databasen. hvis de da får tilgang til koden
from database import db
from database import c

#en loop som passer på at det minst er to tall
kalk=1
for kalk in range(2):
    tall1=int(input("Skriv tall her:"))
    tall2=int(input("Skriv tall her:"))
    avslutt=str(input("Skriv j hvis du er ferdig med å taske inn tall. N for å fortsette:"))
    #her bruker jeg if for å gi valge til brukeren hvis brukeren vil ha mer en to tall.
    if avslutt == "j" or "J":
        pass  
    if avslutt == "n" or "N":
        break

class Kalk:
    #Her har jeg en funksjon som innerholder selve kalkulatoren
    #Jeg måtte og lage en ny test mappe for å lage test modull med den forventende svaret returneres. Se her:
    #den simulerte funksjonen som vil funke sikt def tegn funker
    #def kalk():
        #i = 1+1
        #print(i)
        #return 2
    #Her er den jeg testa med:
    #import kalk
    #def test_kalk():
        #assert kalk(2) == 2

    def tegn():
        t=input("Skriv inn tegn:")
        #ovenfor bruker jeg t variableren for å la brukeren slå inn hva kalkulatoren skal gjøre og if for å utføre det brukeren vil som feks. Hvis bruker slår inn '+' vil programmet legge sammen
        if t == ("+"):
            return tall1+tall2
        if t == ("-"):
            return tall1-tall2
        if t == ("/"):
            return tall1/tall2
        if t == ("*"):
            return tall1*tall2
    #Her gir jeg funksjonen til variabel r. dette gjør jeg for å legge resultatet av regnestykke i databasen nedenfor.
    r=tegn()

    #Her spør jeg om navnet til brukeren og hvilken dato brukeren regner.
    user_navn=input("Skriv ditt navn:")
    user_dato=input("Skriv din nåværende dato:")
    #Her printer jeg ut resultatet av regnestykket brukeren regner.
    print(r)

    #Her legge jeg til data som bruker har gitt som navn, samt resultatet av regnestykke.
    #Her bruker jeg insert kommandoen med de variablene som innerholder navnet, dato osv
    c.execute("insert into Input(navn, resultat, dato) values('{}', {}, '{}')".format(user_navn, r, user_dato))
    #commit er for å bekrefte den kommandoen ovenfor.
    db.commit()
    db.close()