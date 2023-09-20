"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som _sleepiness, _thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner:
    def __init__(self):
        self._sleepiness = 0
        self._thirst = 0
        self._hungry = 0
        self._whisky = 0
        self._gold = 0
        self.slept = 0  # from here down it is a 'turns' counter
        self.mined = 0
        self.ate = 0
        self.shopped = 0
        self.drank = 0
        self.isalive = True

    def eat(self):
        self._sleepiness += 5
        self._thirst -= 5
        self._hungry -= 20
        self._gold -= 2  # food price? maybe
        self.condition("Eat ")
        self.ate += 1

    def shop(self):
        self._sleepiness += 5
        self._thirst += 1
        self._hungry += 1
        self._whisky += 1
        self._gold -= 1
        self.condition("Shop")
        self.shopped += 1

    def drink(self):
        self._sleepiness += 5
        self._thirst -= 15
        self._hungry -= 1
        self._whisky -= 1
        self.condition("Drink")
        self.drank += 1

    def sleep(self):
        self._sleepiness -= 10
        self._thirst += 1
        self._hungry += 1
        self.condition("Sleep")
        self.slept += 1

    def mine(self):
        self._sleepiness += 5
        self._thirst += 5
        self._hungry += 5
        self._gold += 5
        self.condition("Mine")
        self.mined += 1

    def condition(self, activity):  # prints current 'stats' and checks if miner has pushed beond limits and therefore died
        print(f"{activity}\t \t Sleepiness: {self._sleepiness} Thirst: {self._thirst} Hungry: {self._hungry} Whisky {self._whisky} Gold: {self._gold}\t", end=" ")
        if self._sleepiness > 100 or self._thirst > 100 or self._hungry > 100 or self._whisky > 10:
            self.death()

    def death(self):
        self.isalive = False

    def choosetoday(self):  # what to do on any given day so as to not die
        if self._sleepiness < 96 and self._hungry > 94 and self._gold >= 2:
            self.eat()
        elif self._sleepiness < 91 and self._thirst > 87 and self._gold >= 1:
            self.shop()
        elif self._sleepiness < 96 and self._whisky >= 1:
            self.drink()
        elif self._sleepiness > 99:
            self.sleep()
        else:
            self.mine()


morris = Miner()
# dead or alive - conditions for day activity - stop at day 1000
for day in range(1000):  # 1000 days
    if morris.isalive:
        morris.choosetoday()
        print(day + 1)
    else:
        print("\n\t\t Morries R.I.P  \n")
        break  # if he dies stop the count
print(f"\n\tHe mined {morris.mined} times, slept {morris.slept} days, ate {morris.ate} meals, bought whisky {morris.shopped} times and drank {morris.drank} bottels of whisky")
