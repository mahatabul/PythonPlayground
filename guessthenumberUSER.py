import random

def computerguess(x):
    low = 1
    high = x
    comment = ''
    while comment!="c":
        guess = random.randint(low, high)
        comment = input(f"my guess {guess} is too high (H) or low (L) or correct (C) ?? =").lower()
        if comment=="l":
            low+=1
        elif comment == "h":
            high-=1
        else:
            print("You guessed it correct !! The number is =", guess)
            break



print(" Hello User \n Give me a range and i will guess the number. \n Now Input a range.")
range = int(input(" range = "))
computerguess(range)



