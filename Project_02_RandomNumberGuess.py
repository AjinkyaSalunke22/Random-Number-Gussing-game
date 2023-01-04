import random

x = (random.randrange(1,10))



userChance = 0 
highscore = 0

y = None

# you can uncomment it for your reference.
# print("Number choosen by computer ...", + x)


while (userChance <=  3):

    y = int(input(f"***** Please guess the random number from '1' to '10' ... Current chance is {userChance} out of 3 ***** \n"))
    if(x % 2 == 0 and userChance < 3):
        print(f" HINT: Guess the number which is even number .\n")
    if(x % 2 != 0 and userChance < 3):
        print(f" HINT: Guess the number which is odd number .\n")
    if (x < y and userChance < 3):
        print(f" HINT: Guess the number which is less than the past number .\n")
    elif(y < x and userChance < 3):
        print(f" HINT: Guess the number which is greater than the past number .\n")
    elif(y == x ):
        print(f"***** You won the game !!! In {userChance} chances. *****\n" )
        userChance = 3
        highscore = highscore + 1

        if(highscore > 0):
            with open('Project_02_GameScore.txt', 'w') as f:
                f.write("High Score of the user is :- \n")
                f.write(str(highscore))
                print("Score updated !!! and recorded in GameScore File. \n")
            
                yn = input("Want to play the game again ? {y/n} \n")

            if (yn == "y"):
                userChance = 1
                x = (random.randrange(1,10))

                # you can uncomment it for your reference.
                # print("New no by Computer is ", + x)

            elif( yn == "n"):
                userChance = 3
            else:
                print("---xxxxx---  Incorrect choice :( Game EXITED !!! ---xxxxx---")

    elif(userChance == 3):
        print(f"You loose the game :( \n")
        yn = input("***** Your chances are over ... Want to play the game again ? {y/n} *****\n")

        if (yn == "y"):
            userChance = 1
        elif( yn == "n"):
            userChance = 3
            print("---xxxxx--- We will miss you :( Game EXITED !!! ---xxxxx---")
        else:
            userChance = 3
            print("---xxxxx--- Wrong choice :( Game EXITED !!! ---xxxxx---")
            
  

    userChance = userChance + 1
print("---xxxxx--- game Exited !!! ---xxxxx---")






   
    
    

