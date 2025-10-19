# GAME - LADDER AND SNAKE
print("Rule - A Die will Roll."
      "\n       Depending on the Points you will move forward."
      "\n       Who reach first from the position 0 to 100 will be the winner.")
print("")
print("There are Ladders in"
      "\n[5 will send you to position no.58],"
      "\n[14 will send you to position no.49],"
      "\n[47 will send you to position no.60],"
      "\n[53 will send you to position no.72],"
      "\n[64 will send you to position no.83]"
      "\n[75 will send you to position no.94]")
print("")
print("There are Snakes in"
      "\n[38 will send you to position no.20],"
      "\n[45 will send you to position no.07],"
      "\n[51 will send you to position no.10],"
      "\n[65 will send you to position no.54],"
      "\n[91 will send you to position no.73]"
      "\n[97 will send you to position no.61]")
print("")
Choice=(input("Do you want to start the game now? (yes or no) "))
print("")
if Choice=="no":
    print("Let's Quit the Game")
if Choice!="yes" and Choice!="no":
    print("You Have Typed Invalid Option")
    print("Restart and Please Type 'yes' or 'no'")
if Choice=="yes":
    print("\n There are 2 Player. You and Computer. Both have 1 chance to roll the dice in a order."
          "\n you and Computer will be at 0th Position untill the Dice face up to 1 to start the Game")
    print("")
    print("Let's Starts the Game!")
    print("")
    Computer_Position=0
    Player_Position=0
    Player_Starting_Position=0
    Computer_Starting_Position=0
    i=1
    while Computer_Starting_Position==0 or Computer_Position!=0:
        Chance=input("Computer Turns. Press Enter Button to Roll The Die ")
        if Chance=="":
            from random import *
            Points=randrange(1,6)
            print("Computer Got ",Points)
            temp=Points
            if Computer_Position!=0:
                Computer_Position=Computer_Position+Points
                if True:
                    if Computer_Position>=1 and Computer_Position<=4 and i==1:
                        print("Hint: Ladder available in 5th Position. It takes to 58")
                        i=0
                    elif Computer_Position>=8 and Computer_Position<=13 and i==0:
                        print("Hint: Ladder available in 14th Position. It takes to 49")
                        i=1
                    elif Computer_Position>=32 and Computer_Position<=37 and i==1:
                        print("Snake is there in 38")
                        i=0
                    elif Computer_Position>=36 and Computer_Position<=41 and i==0:
                        print("Hint: Ladder available in 42nd Position. It takes to 60")
                        i=1
                    elif Computer_Position>=39 and Computer_Position<=44 and i==1:
                        print("Snake is there in 45")
                        i=0
                    elif Computer_Position>=46 and Computer_Position<=50 and i==0:
                        print("Snake is there in 51")
                        i=1
                    elif Computer_Position>=48 and Computer_Position<=52 and i==1:
                        print("Hint: Ladder available in 53rd Position. It takes to 72")
                        i=0
                    elif Computer_Position>=58 and Computer_Position<=63 and i==0:
                        print("Hint: Ladder available in 64th Position. It takes to 83")
                        i=1
                    elif Computer_Position>=59 and Computer_Position<=64 and i==1:
                        print("Snake is there in 65")
                        i=0
                    elif Computer_Position>=69 and Computer_Position<=74 and i==0:
                        print("Hint: Ladder available in 75th Position. It takes to 94")
                        i=1
                    elif Computer_Position>=85 and Computer_Position<=90 and i==1:
                        print("Snake is there in 91")
                        i=0
                    elif Computer_Position>=92 and Computer_Position<=96 and i==0:
                        print("Snake is there in 97")
                        i=1
                if Computer_Position==5:
                        Computer_Position=58
                        print("Computer used the Ladder in 5")
                elif Computer_Position==14:
                        Computer_Position=49
                        print("Computer used the Ladder in 14 ")
                elif Computer_Position==38:
                        Computer_Position=20
                        print("Snake Attacked in 38")
                elif Computer_Position==42:
                        Computer_Position=60
                        print("Computer used the Ladder in 42")
                elif Computer_Position==45:
                        Computer_Position=7
                        print("Snake Attacked in 45")
                elif Computer_Position==51:
                        Computer_Position=10
                        print("Snake Attacked in 51")
                elif Computer_Position==53:
                        Computer_Position=72
                        print("Computer used the Ladder in 53")
                elif Computer_Position==64:
                        Computer_Position=83
                        print("Computer used the Ladder in 64")
                elif Computer_Position==65:
                        Computer_Position=54
                        print("Snake Attacked in 65")
                elif Computer_Position==75:
                        Computer_Position=94
                        print("Computer used the Ladder in 75")
                elif Computer_Position==91:
                        Computer_Position=73
                        print("Snake Attacked in 91")
                elif Computer_Position==97:
                        Computer_Position=61
                        print("Snake Attacked in 97")                
            elif temp==1 and Computer_Position==0:
                 print("Computer is free to move forward now.")
                 #Computer_Starting_Position=temp
                 #Computer_Position=Computer_Starting_Position
                 Computer_Position=temp
        if Computer_Position<100:
            print("Computer_Current_Position is ",Computer_Position)
            print("")
        if Computer_Position>=100:
            print("Computer has won the Game. It Reached 100")
            break
#------------------------------------------------------------------------------------------------------
        Chance=input("Your Turns. Press Enter Button to Roll The Die ")
        if Chance=="":
            from random import *
            Points=randrange(1,6)
            print("You got ", Points)
            temp=Points
            if Player_Position!=0:
                Player_Position=Player_Position+Points
                if True:
                    if Player_Position>=1 and Player_Position<=4 and i==1:
                        print("Hint: Ladder available in 5th Position. It takes to 58")
                        i=0
                    elif Player_Position>=8 and Player_Position<=13 and i==0:
                        print("Hint: Ladder available in 14th Position. It takes to 49")
                        i=1
                    elif Player_Position>=32 and Player_Position<=37 and i==1:
                        print("Snake is there in 38")
                        i=0
                    elif Player_Position>=36 and Player_Position<=41 and i==0:
                        print("Hint: Ladder available in 42nd Position. It takes to 60")
                        i=1
                    elif Player_Position>=39 and Player_Position<=44 and i==1:
                        print("Snake is there in 45")
                        i=0
                    elif Player_Position>=46 and Player_Position<=50 and i==0:
                        print("Snake is there in 51")
                        i=1
                    elif Player_Position>=48 and Player_Position<=52 and i==1:
                        print("Hint: Ladder available in 53rd Position. It takes to 72")
                        i=0
                    elif Player_Position>=58 and Player_Position<=63 and i==0:
                        print("Hint: Ladder available in 64th Position. It takes to 83")
                        i=1
                    elif Player_Position>=59 and Player_Position<=64 and i==1:
                        print("Snake is there in 65")
                        i=0
                    elif Player_Position>=69 and Player_Position<=74 and i==0:
                        print("Hint: Ladder available in 75th Position. It takes to 94")
                        i=1
                    elif Player_Position>=85 and Player_Position<=90 and i==1:
                        print("Snake is there in 91")
                        i=0
                    elif Player_Position>=92 and Player_Position<=96 and i==0:
                        print("Snake is there in 97")
                        i=1
                if Player_Position==5:
                        Player_Position=58
                        print("Computer used the Ladder in 5")
                elif Player_Position==14:
                        Player_Position=49
                        print("Computer used the Ladder in 14 ")
                elif Player_Position==38:
                        Player_Position=20
                        print("Snake Attacked in 38")
                elif Player_Position==42:
                        Player_Position=60
                        print("Computer used the Ladder in 42")
                elif Player_Position==45:
                        Player_Position=7
                        print("Snake Attacked in 45")
                elif Player_Position==51:
                        Player_Position=10
                        print("Snake Attacked in 51")
                elif Player_Position==53:
                        Player_Position=72
                        print("Computer used the Ladder in 53")
                elif Player_Position==64:
                        Player_Position=83
                        print("Computer used the Ladder in 64")
                elif Player_Position==65:
                        Player_Position=54
                        print("Snake Attacked in 65")
                elif Player_Position==75:
                        Player_Position=94
                        print("Computer used the Ladder in 75")
                elif Player_Position==91:
                        Player_Position=73
                        print("Snake Attacked in 91")
                elif Player_Position==97:
                        Player_Position=61
                        print("Snake Attacked in 97")
            elif temp==1 and Player_Position==0:
                print("You are free to move forward now.")
                #Player_Starting_Position=temp
                #Player_Position=Player_Starting_Position
                Player_Position=temp
        if Player_Position<100:
            print("Player_Current_Position is ",Player_Position)
            print("")
        if Player_Position>=100:
            print("Player won the Game. Player Reached 100")
            break

    
    
    
    
      
