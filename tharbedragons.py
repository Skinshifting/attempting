from sys import exit

# Start
def start():
        print "While out walking in the woods, you find an old tree covered in vines."
        print "The tree is so beautiful you decide to take a closer look."
        print "As you run your hand along the trunk covered in vines you find
the tree has a large hole."
        print "You pull back the vines and peer in..."
        print "Suddenly someone or something pushes you from behind and you
fall into the hole."
        print "You fall and hit the ground hard, feeling a little dazed you
take a look around."
        print "You see torches all along the wall and a long hallway before you."
        print "You walk further down the hallway and notice three doors."
        print "Each are numbered: 1, 2, 3."
        print "You also notice a keypad located on the wall."
        print "Choose a room or they keypad."
        rooms()

pocket = []

def rooms():

        while True:

                choice = raw_input("> ")

                if choice == "1":
                        dusty_room()
                elif choice == "2":
                        goblin_room()
                elif choice == "3":
                        dragon_room()
                elif choice == "keypad":
                        keypad()
                else:
                        print "Please enter 1 2 3 or keypad"

def dusty_room():
        print "You enter the room to find it covered in cobwebs and dust."
        print "There is some old wooden chairs and tables, they look they
haven't been used in ages."
        print "Would you like to take a look around or head back out into the hallway?"

        choice = raw_input("> ")

        if "hallway" in choice:
                hallway()
        if "look" in choice:
                trap_door()

def goblin_room():
        print "You enter the room and look around..."
        print "All of the sudden a goblin jumps on top of you licking his lips!"
        print "He takes a bite out of you and you go running back into the hallway."
        hallway()

def dragon_room():
        print "You walk into the room and peer at a very large sleeping dragon."
        print "He is covered in red scales and is snoring very loudly."
        print "You see a shiny key hanging on the wall behind the dragon."
        print "You decide you want the key, will you sneak left or right?"

        choice = raw_input("> ")

        if choice == "left":
                print "You trip and land on the dragon, he wakes up, yawns and eats
you in one bite."
        elif choice == "right":
                print "You slowly sneak past him and successfully grab the key. You
run back out to the hallway."
                pocket.append('key')
                hallway()
        else:
                print "Your pea sized brain does not compute. Choose left or right."

def keypad():
        print "You approach a 10 digit keypad, would you like to try a number?"

        choice = raw_input("> ")

        if choice == "yes":
                keypad_choice()
        elif choice =="no":
                hallway()
        exit(0)

def hallway():
        print "You are back in the hallway, would you like to choose another
room or try the keypad?"
        rooms()

def trap_door():
        print "You find a trap door, but it is locked, do you have a key?"

        choice = raw_input("yes or no? ")

        if choice == "yes" and 'key' in pocket:
                print "You open the trap door!"
                print "You find an empty room but painted on the wall is four large numbers."
                print "The numbers from left to right read: 8 5 3 9"
                print "Would you like to try this number on the keypad?"

                choice = raw_input("yes or no? ")

                if choice == "yes":
                        print "You exit the room and approach the keypad."
                        keypad()
                elif choice == "no":
                        print "Then choose where you want to go..."
                        hallway()

        elif choice == "yes" and 'key' not in pocket:
                print "Liar. You should probably go find one."
                hallway()
        elif choice == "no":
                print "I would go find that key."
                hallway()

        exit(0)

def correct():
        print "You hear a loud noise and a door begins to slowly open..."
        print "...you think you hear something inside..."
        print "You back up a little and when the door finally reaches door level..."
        print "You see a giant pile of gold and riches!"

def keypad_choice():
        print "What numbers would you like to try?"

        choice = raw_input("> ")

        if "8539" in choice:
                correct()
        elif "8539" not in choice:
                print "That is not correct."
                print "Would you like to try again?"

                choice = raw_input("> ")

                if choice == "yes":
                        keypad_choice()
                elif choice == "no":
                        hallway()


start()
