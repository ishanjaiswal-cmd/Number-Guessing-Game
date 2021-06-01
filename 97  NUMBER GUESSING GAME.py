import random

print("LETS PLAY A GUESSING GAME")

nummm = random.randint(1,9)

chances = 0

print("GUESS ANY NUMBER BETWEEN 1 To 9")


while chances<5:
    guess = int(input("ENTER YOUR GUESS : "))

    if guess == nummm:
        print("CONGRATULATION YOU WON!!")
        break
    
    elif guess < nummm:
        print("YOUR GUES IS TOO LOW")
        print("GUESS A NUMBER HIGHER THAN THIS : ")

    else:
        print("YOUR GUESS IS TOO HIGH.")
        print("GUESS A NUMBER LESSER THAN THIS : ")
    
    chances+=1

if chances==5 and guess!= nummm:
    print("YOU LOSE!!! The number is", nummm)

