# GAME - LADDER AND SNAKE
print("A die will be rolled."
      "\n       “Depending on the points, you will move forward."
      "\n       “Whoever reaches first from position 0 to 100 will be the winner.")
print("")
print("There is a ladder at the position, "
      "\n[5 will send you to position 58]"
      "\n[14 will send you to position 49]"
      "\n[47 will send you to position 60]"
      "\n[53 will send you to position 72]"
      "\n[64 will send you to position 83]"
      "\n[75 will send you to position 94]")
print("")
print("There is a Snake at the position, "
      "\n[38 will send you to position 20]"
      "\n[45 will send you to position 07]"
      "\n[51 will send you to position 10]"
      "\n[65 will send you to position 54]"
      "\n[91 will send you to position 73]"
      "\n[97 will send you to position 61]")
print("")
Choice=(input("Do you want to start the game now? (yes or no) "))
print("")
if Choice=="no":
    print("Let’s end the game.")
if Choice!="yes" and Choice!="no":
    print("You have typed an invalid option.")
    print("To Restart, please type ‘yes’ or ‘no’.")
if Choice=="yes":
    print("\n There are 2 players: you and the computer. Each has one chance to roll the dice in turn."
          "\n You and the computer will stay at position 0 until the Dice face up to 1 to start the Game")
    print("")
    print("Let’s start the game!")
    print("")
    Computer_Position=0
    Player_Position=0
    Player_Starting_Position=0
    Computer_Starting_Position=0
    i=1
    while Computer_Starting_Position==0 or Computer_Position!=0:
        Chance=input("Computer’s turn. Press the Enter key to roll the die.")
        if Chance=="":
            from random import *
            Points=randrange(1,6)
            print("The computer got ",Points)
            temp=Points
            if Computer_Position!=0:
                Computer_Position=Computer_Position+Points
                if True:
                    if Computer_Position>=1 and Computer_Position<=4 and i==1:
                        print("Hint: A ladder is at position 5. It takes you to position 58.")
                        i=0
                    elif Computer_Position>=8 and Computer_Position<=13 and i==0:
                        print("Hint: A ladder is at position 14. It takes you to position 49.")
                        i=1
                    elif Computer_Position>=32 and Computer_Position<=37 and i==1:
                        print("A snake is at position 38.")
                        i=0
                    elif Computer_Position>=36 and Computer_Position<=41 and i==0:
                        print("Hint: A ladder is at position 42. It takes you to position 60.")
                        i=1
                    elif Computer_Position>=39 and Computer_Position<=44 and i==1:
                        print("A snake is at position 45.")
                        i=0
                    elif Computer_Position>=46 and Computer_Position<=50 and i==0:
                        print("A snake is at position 51.")
                        i=1
                    elif Computer_Position>=48 and Computer_Position<=52 and i==1:
                        print("Hint: A ladder is at position 53. It takes you to position 72.")
                        i=0
                    elif Computer_Position>=58 and Computer_Position<=63 and i==0:
                        print("Hint: A ladder is at position 64. It takes you to position 83.")
                        i=1
                    elif Computer_Position>=59 and Computer_Position<=64 and i==1:
                        print("A snake is at position 65.")
                        i=0
                    elif Computer_Position>=69 and Computer_Position<=74 and i==0:
                        print("Hint: A ladder is at position 75. It takes you to position 94.")
                        i=1
                    elif Computer_Position>=85 and Computer_Position<=90 and i==1:
                        print("A snake is at position 91.")
                        i=0
                    elif Computer_Position>=92 and Computer_Position<=96 and i==0:
                        print("A snake is at position 97.")
                        i=1
                if Computer_Position==5:
                        Computer_Position=58
                        print("The computer used the ladder at position 5.")
                elif Computer_Position==14:
                        Computer_Position=49
                        print("The computer used the ladder at position 14.")
                elif Computer_Position==38:
                        Computer_Position=20
                        print("A snake attacked at position 38.")
                elif Computer_Position==42:
                        Computer_Position=60
                        print("The computer used the ladder at position 42.")
                elif Computer_Position==45:
                        Computer_Position=7
                        print("A snake attacked at position 45.")
                elif Computer_Position==51:
                        Computer_Position=10
                        print("A snake attacked at position 51.")
                elif Computer_Position==53:
                        Computer_Position=72
                        print("The computer used the ladder at position 53.")
                elif Computer_Position==64:
                        Computer_Position=83
                        print("The computer used the ladder at position 64.")
                elif Computer_Position==65:
                        Computer_Position=54
                        print("A snake attacked at position 65.")
                elif Computer_Position==75:
                        Computer_Position=94
                        print("The computer used the ladder at position 75.")
                elif Computer_Position==91:
                        Computer_Position=73
                        print("A snake attacked at position 91.")
                elif Computer_Position==97:
                        Computer_Position=61
                        print("A snake attacked at position 97.")                
            elif temp==1 and Computer_Position==0:
                 print("The computer is ready to move forward.")
                 #Computer_Starting_Position=temp
                 #Computer_Position=Computer_Starting_Position
                 Computer_Position=temp
        if Computer_Position<100:
            print("Computer_Current_Position is ",Computer_Position)
            print("")
        if Computer_Position>=100:
            print("The computer has won the game. It reached 100.")
            break
#------------------------------------------------------------------------------------------------------
        Chance=input("Your turn. Press the Enter key to roll the die. ")
        if Chance=="":
            from random import *
            Points=randrange(1,6)
            print("You got ", Points)
            temp=Points
            if Player_Position!=0:
                Player_Position=Player_Position+Points
                if True:
                    if Player_Position>=1 and Player_Position<=4 and i==1:
                        print("Hint: A ladder is available at the 5th position. It takes you to 58.")
                        i=0
                    elif Player_Position>=8 and Player_Position<=13 and i==0:
                        print("Hint: A ladder is available at the 14th position. It takes you to 49.")
                        i=1
                    elif Player_Position>=32 and Player_Position<=37 and i==1:
                        print("A snake is at position 38.")
                        i=0
                    elif Player_Position>=36 and Player_Position<=41 and i==0:
                        print("Hint: A ladder is available at the 42nd position. It takes you to 60.")
                        i=1
                    elif Player_Position>=39 and Player_Position<=44 and i==1:
                        print("A snake is at position 45.")
                        i=0
                    elif Player_Position>=46 and Player_Position<=50 and i==0:
                        print("A snake is at position 51.")
                        i=1
                    elif Player_Position>=48 and Player_Position<=52 and i==1:
                        print("Hint: A ladder is available at the 53rd position. It takes you to 72.")
                        i=0
                    elif Player_Position>=58 and Player_Position<=63 and i==0:
                        print("Hint: A ladder is available at the 64th position. It takes you to 83.")
                        i=1
                    elif Player_Position>=59 and Player_Position<=64 and i==1:
                        print("A snake is at position 65.")
                        i=0
                    elif Player_Position>=69 and Player_Position<=74 and i==0:
                        print("Hint: A ladder is available at the 75th position. It takes you to 94.")
                        i=1
                    elif Player_Position>=85 and Player_Position<=90 and i==1:
                        print("A snake is at position 91.")
                        i=0
                    elif Player_Position>=92 and Player_Position<=96 and i==0:
                        print("A snake is at position 97.")
                        i=1
                if Player_Position==5:
                        Player_Position=58
                        print("The computer used the ladder at position 5")
                elif Player_Position==14:
                        Player_Position=49
                        print("The computer used the ladder at position 14 ")
                elif Player_Position==38:
                        Player_Position=20
                        print("A snake attacked at position 38")
                elif Player_Position==42:
                        Player_Position=60
                        print("The computer used the ladder at position 42")
                elif Player_Position==45:
                        Player_Position=7
                        print("A snake attacked at position 45")
                elif Player_Position==51:
                        Player_Position=10
                        print("A snake attacked at position 51")
                elif Player_Position==53:
                        Player_Position=72
                        print("The computer used the ladder at position 53")
                elif Player_Position==64:
                        Player_Position=83
                        print("The computer used the ladder at position 64")
                elif Player_Position==65:
                        Player_Position=54
                        print("A snake attacked at position 65")
                elif Player_Position==75:
                        Player_Position=94
                        print("The computer used the ladder at position 75")
                elif Player_Position==91:
                        Player_Position=73
                        print("A snake attacked at position 91")
                elif Player_Position==97:
                        Player_Position=61
                        print("A snake attacked at position 97")
            elif temp==1 and Player_Position==0:
                print("You are free to move forward now.")
                #Player_Starting_Position=temp
                #Player_Position=Player_Starting_Position
                Player_Position=temp
        if Player_Position<100:
            print("Player_Current_Position is ",Player_Position)
            print("")
        if Player_Position>=100:
            print("The Player won the Game. The Player reached 100")
            break

    
    
    
    
      
