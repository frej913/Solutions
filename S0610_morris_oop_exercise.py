"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner:
    def __init__(self):
        self.sleepiness = 0
        self.thirst = 0
        self.hungry = 0
        self.whisky = 0
        self.gold = 0
        self.slept = 0  # from here down it is a 'turns' counter
        self.mined = 0
        self.ate = 0
        self.shopped = 0
        self.drank = 0

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hungry -= 20
        self.gold -= 2  # food price? maybe
        print("Eat")
        self.ate += 1

    def shop(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hungry += 1
        self.whisky += 1
        self.gold -= 1
        print("shop")
        self.shopped += 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hungry -= 1
        self.whisky -= 1
        print("drink")
        self.drank += 1

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hungry += 1
        print("sleep")
        self.slept += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hungry += 5
        self.gold += 5
        print("mine")
        self.mined += 1
