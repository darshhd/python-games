import random
print("Game of guess the number")
ready=str(input("Are you ready to play, press Y for yes and N for no:"))
if (ready=="Y" or ready=="y"):
    myname=str(input("Enter your name:"))
    print(f'Hello there {myname}, you will have 6 chances to guess the number between 1 and 20')
    chances=0
    guessednumber = random.randint(1,20)

    while chances <= 6:
        mynum=int(input("Enter a number:"))
        if mynum >= 1 and mynum <=20:
            chances+=1
            if mynum == guessednumber:
                break
            elif mynum > guessednumber:
                print("The guessed number is less than this try again")
            elif mynum < guessednumber:
                print("The guessed number is greater than this try again")
            elif (mynum > 20 and mynum < 1):
                print("Number exceeded, try again")
        else:
            print("number invalid")
            exit()

    if mynum == guessednumber:
        print(f'You are right!, the guessed number is {mynum}')
    elif mynum != guessednumber:
        print(f'You lost the game, the guessed number was {guessednumber}')


elif(ready=="N" or ready=="n"):
    print("Goodbye!")
else:
    print("invalid input try again")
