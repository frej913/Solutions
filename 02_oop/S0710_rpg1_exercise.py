"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
_current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Tilføj en klasse "Healer", som arver fra klassen Character.
En healer har attackpower=0 men den har en ekstra attribut "healpower".

Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Character:
    def __init__(self, name, max_health, attackpower):  # had 'current_health,' but prob don't need it
        self.name = name
        self.max_health = max_health
        self._current_health = max_health  # always start with full health
        self.attackpower = attackpower

    def __repr__(self):
        return f"Name: {self.name}.\tHP: {self._current_health}/{self.max_health}.\tAttack: {self.attackpower}"

    def hit(self, victim):
        print("hit you")
        victim.get_hit(self.attackpower)

    def get_hit(self, attacked):
        print(f"{self.name} was hit")
        self._current_health -= attacked
        if self._current_health < 0:
            self._current_health = 0
            print("death")  # maybe death method or bool for other checks,

    def get_healed(self, healed):
        print(f"{self.name} was healed")
        self._current_health += healed
        if self._current_health > self.max_health:
            self._current_health = self.max_health


class Healer(Character):
    def __init__(self, name, max_health, healpower):
        super().__init__(name, max_health, 0)
        self.healpower = healpower

    def __repr__(self):
        return f"Name: {self.name}.\tHP: {self._current_health}/{self.max_health}.\tHealing: {self.healpower}"

    def heal(self, target):
        print("HEAL")
        target.get_healed(self.healpower)


warrior = Character("Bo", 80, 10)
archer = Character("Ib", 65, 12)
healer1 = Healer("Kim", 50, 11)

people = [warrior, archer, healer1]
for person in people:
    print(person)

warrior.hit(archer)

for person in people:
    print(person)

archer.hit(warrior)

for person in people:
    print(person)

healer1.heal(warrior)
healer1.heal(archer)

for person in people:
    print(person)
