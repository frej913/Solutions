"""
Opgave "Tom the Turtle":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig side_size i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        side_size: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    sq_size = 240
    if -sq_size < turtle_name.position()[0] < sq_size and -sq_size < turtle_name.position()[1] < sq_size:
        return 1
    # you will need this: x-value: turtle_name.position()[0]
    # and this:           y-value: turtle_name.position()[1]
    return 0

def square(length, tom):
    for x in range(4):
        tom.forward(length)
        tom.left(90)
        print(visible(tom))


# Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
#     Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
#     Funktionen skal have nogle parametre. F.eks:
#         antal: hvor mange firkanter skal der tegnes?
#         størrelse: hvor store er firkanterne?
#         afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?
def many_squares(antal, side_size, afstand):
    tom = turtle.Turtle()  # almost just copy-paste
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(antal):
        square(side_size, tom)
        tom.penup()
        tom.forward(afstand)  # kunne lave side_size + afstand så de ikke overlapper
        tom.pendown()
    turtle.done()

def spiral(addlength):
    tom = turtle.Turtle()  # almost just copy-paste
    print(type(tom))
    tom.speed(10)  # fastest: 10, slowest: 1
    length = addlength
    while visible(tom) == 1:
        tom.forward(length)
        tom.left(90)
        length = addlength + length
        print(length)

    turtle.done()

def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


user_input = ""
while user_input != "x":
    print("""What do you want to do?
    1) See the demo
    2) Square
    3) Many squares
    4) Spiral
    x) Stop program""")
    user_input = input()
    if user_input == "1":
        demo()
    elif user_input == "2":
        print("Write the number of pixels you want the square to be:")
        user_in2 = input()
        many_squares(1, user_in2, 0)  # square no longer has a definition for tom 
    elif user_input == "3":
        many_squares(3, 40, 60)  # kunne bede om alle tre men er doven
    elif user_input == "4":
        spiral(5)
    elif user_input == "x":
        print("Ending program.")
    else:
        print("Unknown instruction please try again")
