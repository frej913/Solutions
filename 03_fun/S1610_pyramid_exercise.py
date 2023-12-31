"""Opgave "Number pyramid"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
Funktionen udskriver tallene i hver række og også deres sum.

I hovedprogrammet kalder du funktionen med fx 7 som argument.

Tilføj en mere generel funktion pyramid2.
Denne funktion har som andet parameter "firstline" en liste med pyramidens øverste rækkens tallene.

I hovedprogrammet kalder du pyramid2 med fx 10 som det første argument
og en liste med tal efter eget valg som andet argument.
Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne S1620_pyramid_help.py og starte derfra

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


# Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
# Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
# Funktionen udskriver tallene i hver række og også deres sum.

# I hovedprogrammet kalder du funktionen med fx 7 som argument.


# I took a LOT of inspo from 'solution'
def pyramid(lines):
    start_line = [1, 1]  # the line that is used and printed
    current_line = [i for i in start_line]  # apply changes little at a time before 'official list' is updated
    for x in range(lines):
        print(f"Line {x+1}:", end=" ")
        print(start_line)
        new_stuffs = 0  # this was a total steal
        for y in range(len(start_line)-1):
            if start_line[y] + start_line[y+1] == x + 2:  # is it the right number
                current_line.insert(y+1+new_stuffs, x+2)  # if yes, add it
                new_stuffs += 1  # you check in original list but insert in current list, so it needs an offset
        start_line = [i for i in current_line]


pyramid(7)
