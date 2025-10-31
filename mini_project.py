import random

randomNum=random.randint(1,100)




    


while True:
    guessNum=input("guess the number or Quit(Q):")

    if(guessNum=="Q"):
        break


    guessNum=int(guessNum)
    if(randomNum==guessNum):
        print("Success :Correct...")
        break

    elif(guessNum<randomNum):
        print("Your number was too small.Take a bigger guess..")

    else:
        print("Your number was too big.Take a smaller guess..")


print("....Game Over!")    
