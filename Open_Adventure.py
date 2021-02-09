#This is a choose your own adventure game
#The following is an introduction
import random
print("Hello welcome to Open Adventure!")
print(" ")
print("The goal is to defeat the Boss!")
print(" ")
print("Bonus mission: collect 100 Points!")
print(" ")
print("LET'S BEGIN!")
print(" ")
print("You awake from your bed to find a SWORD and SHIELD next to you, you grab the sword and shield...")
#getting imput from the user
M_CHAR = input('Aww hello young adventurer, my name is Navi what is your name?')
#getting imput from user for other characters name
print("Aww Yes",M_CHAR)
O_CHAR = input("you are the only one who knows the name of the Dark Lord... what was it?")
##creating logical statements
print("Ofcourse! We must stop",O_CHAR)
print(" ")
print("You leave your bedroom, then exit the house.")
i = 1
while i < 2:
    print("You walk down the path you come to a fork in the road.")
    print(" ")
    direction = input("***DO YOU GO RIGHT PRESS(1) OR LEFT PRESS (2)?***")
    print(" ")
    if direction == "1":
        print("After walking a little longer you come across some dark woods. Will you ENTER or RETURN HOME?" )
        print(" ")
        Choice1 = input("***TO ENTER PRESS (1) TO GO HOME PRESS (2)***")
        print(" ")
        if Choice1 == "1":
            print("You enter the scary dark woods.Once inside the woods you come to another fork in the road.")
            print("To the left you see a CAVE and to the right you see a LARGE SCARY CASTLE.")
            print(" ")
            print("*** Will you go LEFT or RIGHT?***")
            Choice1a = input("***TO GO LEFT PRESS (1) TO GO RIGHT PRESS (2)***")
            print(" ")
            if Choice1a == "1":
                    print(" You are attacked by a BEAR!")
                    print(" ")
                    Choice1a1 = input("*** WILL YOU ATTACK PRESS(1) OR DEFEND PRESS (2)")
                    print(" ")
                    if Choice1a1 == "1":
                        print("You use your god strength to defeat the bear! + 25 points")
                        print("You run out the cave and back to the path!")
                    elif Choice1a1 == "2":
                        print("the bear knocks out your shield and eats you.")
                        print("Game over")
                        restart = input("PRESS 1 TO CONTINUE")
                        if restart == "1":
                            print ("RESTART!")
                        elif restart == "2":
                            break;
            elif Choice1a == "2":
                    print("You have entered the castle. You see stairs going UP and DOWN.")
                    print("it looks like a THRONE ROOM is upstairs and a DUNGEON is down stairs.")
                    print(" ")
                    Choice1b = input("***TO GO UP TO THE THRONE ROOM PRESS(1) TO GO DOWN TO THE DUNGEON PRESS(2)***")
                    print(" ")
                    if Choice1b == "1":
                        print(" You enter the throne room!")
                        print(O_CHAR)
                        print("is standing infront of you with a menacing look is THE FINAL BATTLE BEGINS!")
                        print(O_CHAR)
                        print("shoots a FIRE BALL at you!.")
                        print(" ")
                        Choice1c = input("***WILL YOU ATTACK PRESS(1) OR DEFEND PRESS(2)?***")
                        ##Risky attack scenario roll above a 4 to win.
                        print(" ")
                        if Choice1c == "1":
                            print("You both attack each other at the same time! (roll 5 or higher to win!)")
                            print(" ")
                            key = input ("***TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE.***")
                            print(" ")
                            dice = random.randint(1, 6)
                            print(dice)
                            if dice >= 5:
                                print("Your attack was stronger!")
                                print("Using your sword you slice through the fireball then deliver the final blow to.")
                                print(O_CHAR)
                                print("YOU WIN! >=[=========> + 50 Points!")
                                break;
                            elif dice < 5:
                                print("The enemy attack was stronger and you were defeated. GAME OVER")
                                restart = input("PRESS 1 TO CONTINUE")
                                if restart == "1":
                                    print ("RESTART!")
                                elif restart == "2":
                                    break;
                        elif Choice1c == "2":
                            #Safe attack scenario roll above a 2 to win.
                            print("You block the attack giving you a better chance to attack! (roll 3 or higher to win!)")
                            print(" ")
                            key = input ("***TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE.***")
                            print(" ")
                            dice = random.randint(1, 6)
                            print(dice)
                            if dice >= 3:
                                print("Your attack was stronger!")
                                print("Using your sword you slice through the fireball then deliver the final blow to.")
                                print(O_CHAR)
                                print("YOU WIN! >=[=========> + 50 Points!")
                                break;
                            elif dice < 3:
                                print("The enemy attack was stronger and you were defeated. GAME OVER")
                                restart = input("PRESS 1 TO CONTINUE")
                                if restart == "1":
                                    print ("RESTART!")
                                elif restart == "2":
                                    break;
                    elif Choice1b == "2":
                        print(" You enter the dungeon where a creature too ugly to describe attacks you!")
                        print(" ")
                        input("***WILL YOU ATTACK PRESS(1) OR DEFEND PRESS(2)?***")
                        print(" ")
                        if Choice1b == "1":
                            ##Risky attack scenario roll above a 4 to win.
                            print("You both attack each other at the same time! (roll 4 or higher to win!)")
                            print(" ")
                            key = input ("TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE.")
                            print(" ")
                            dice = random.randint(1, 6)
                            print(dice)
                            if dice >= 4:
                                print("Your attack was stronger defeating the enemy! + 10 Points!")
                                print("A powerful force teleports you back to the path...")
                            elif dice < 4:
                                print("The enemy attack was stronger and you were defeated. GAME OVER")
                                restart = input("PRESS 1 TO CONTINUE")
                                if restart == "1":
                                    print ("RESTART!")
                                elif restart == "2":
                                    break;
                        if Choice1b == "2":
                            #Safe attack scenario roll above a 2 to win.
                            print("You block the attack giving you a better chance to attack! (roll 2 or higher to win!)")
                            print(" ")
                            key = input ("***TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE.***")
                            print(" ")
                            dice = random.randint(1, 6)
                            print(dice)
                            if dice >= 2:
                                print("Your attack was stronger defeating the enemy! + 25 Points!")
                                print("A powerful force teleports you back to the path...")
                            elif dice < 2:
                                print("The enemy attack was stronger and you were defeated. GAME OVER")
                                restart = input("PRESS 1 TO CONTINUE")
                                if restart == "1":
                                    print ("RESTART!")
                                elif restart == "2":
                                    break;
        elif Choice1 == "2":
            print("You went home to cry. GAME OVER")
            restart = input("PRESS 1 TO CONTINUE")
            if restart == "1":
                print ("RESTART!")
            elif restart == "2":
                break;

    elif direction == "2":

        print("after walking a little longer you come across a large scary castle. Will you ENTER or RETURN HOME?")
        print(" ")
        Choice2 = input("***TO ENTER PRESS (1) TO GO HOME PRESS (2)***")
        print(" ")
        if Choice2 == "1":
                print("You have entered the castle. You see stairs going UP and DOWN.")
                print("it looks like a THRONE ROOM is upstairs and a DUNGEON is down stairs.")
                print("Will you go UP TO THE THRONE ROOM press(1) or DOWN TO THE DUNGEON press(2)?")
                print(" ")
                Choice2a = input("TO GO UP PRESS(1) TO GO DOWN PRESS(2)")
                print(" ")
                if Choice2a == "1":
                    print(" You enter the throne room!")
                    print("Standing infront of you with a menacing look is")
                    print(O_CHAR)
                    print("THE FINAL BATTLE BEGINS!!")
                    print(O_CHAR)
                    print("shoots a fire ball at you.")
                    Choice2b = input("WILL YOU ATTACK PRESS(1) OR DEFEND PRESS(2)?")
                    print(" ")
                    if Choice2b == "1":
                        print("You both attack each other at the same time! (roll 5 or higher to win!)")
                        key = input ("TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE.***")
                        print(" ")
                        dice = random.randint(1, 6)
                        print(dice)
                        if dice >= 5:
                            print("Your attack was stronger!")
                            print(" using your sword you slice threw the fireball then deliver the final blow to")
                            print(O_CHAR)
                            print("YOU WIN! >=[=========> +50 Points!")
                            break;
                        elif dice < 5:
                            print("The enemy attack was stronger and you were defeated. GAME OVER")
                            restart = input("PRESS 1 TO CONTINUE")
                            if restart == "1":
                                print ("RESTART!")
                            elif restart == "2":
                                break;
                    if Choice2b == "2":
                        print("You block the attack giving you a better chance to attack! (roll 3 or higher to win!)")
                        print(" ")
                        key = input ("***TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE.***")
                        print(" ")
                        dice = random.randint(1, 6)
                        print(dice)
                        if dice >= 3:
                            print("Your attack was stronger!")
                            print("using your sword you slice through***")
                            print(O_CHAR)
                            print("YOU WIN! >=[=========> +50 Points!")
                            break;
                        elif dice < 3:
                            print("The enemy attack was stronger and you were defeated. GAME OVER")
                            restart = input("PRESS 1 TO CONTINUE")
                            if restart == "1":
                                print ("RESTART!")
                            elif restart == "2":
                                break;
                elif Choice2a == "2":
                    print(" You enter the dungeon where a creature too ugly to describe attacks you!")
                    print(" ")
                    Choice2b2 = input("***WILL YOU ATTACK PRESS(1) OR DEFEND PRESS(2)?***")
                    if Choice2b2 == "1":
                        print("You both attack each other at the same time! (roll 4 or higher to win!)")
                        key = input ("TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE")
                        dice = random.randint(1, 6)
                        print(dice)
                        if dice >= 4:
                            print("Your attack was stronger defeating the enemy! + 25 Points!")
                            print("A powerful force teleports you back to the path...")
                        elif dice < 4:
                            print("The enemy attack was stronger and you were defeated. GAME OVER")
                            restart = input("PRESS 1 TO CONTINUE")
                            if restart == "1":
                                print ("RESTART!")
                            elif restart == "2":
                                break;
                    if Choice2b2 == "2":
                        print("You block the attack giving you a better chance to attack! (roll 2 or higher to win!)")
                        print(" ")
                        key = input ("***TYPE ANY KEY AND PRESS ENTER TO ROLL THE DICE***")
                        print(" ")
                        dice = random.randint(1, 6)
                        print(dice)
                        if dice >= 2:
                            print("Your attack was stronger defeating the enemy! + 25 Points!")
                            print("A powerful force teleports you back to the path...")
                        elif dice < 2:
                            print("The enemy attack was stronger and you were defeated. GAME OVER")
                            restart = input("PRESS 1 TO CONTINUE")
                            if restart == "1":
                                print ("RESTART!")
                            elif restart == "2":
                                break;
        elif Choice2 == "2":
                print("You went home to cry. GAME OVER")
                restart = input("PRESS 1 TO CONTINUE")
                if restart == "1":
                    print ("RESTART!")
                elif restart == "2":
                    break;
