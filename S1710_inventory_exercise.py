"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Se de første 3 minutter af denne video:
https://www.youtube.com/watch?v=rBU9E-ZOZAI

Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
Funktionen udskriver tallene i hver række.

Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
et bestemt antal optræder i den aktuelle talrække.

I hovedprogrammet kalder du inventory() med fx 6 som argument.

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du kigge på løsningen
i S1720_inventory_solution.py

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

# first itteration used 10-15 min
def inventory(lines):
    for line in range(lines):
        isnot0 = True
        print(line + 1, end=": ")
        while isnot0:
            print("count and print", end=" ")  # create actual code / do this
            isnot0 = False  # replace with if statement
        print("hey")

# i looked a bit (a lot) at solution for inspo -- yes most of the naming are complete rip-offs
def count_numbers(number):
    counter = 0
    for row in rows:
        counter += row.count(number)
    return counter

def inventory2(lines):
    for line in range(lines):
        print(line, end=": ")  # så man kan se hvad linje det er - kinda redundant
        row = []
        rows.append(row)
        column = 0
        apperences = count_numbers(column)
        while apperences > 0:
            row.append(apperences)
            column += 1
            apperences = count_numbers(column)
        row.append(0)
        print(row)


rows = []  # could place at start of function
inventory2(5)
