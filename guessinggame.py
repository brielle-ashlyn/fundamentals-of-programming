from random import randrange 
x = randrange(1, 101)
tryH = 0
tryL = 0
tryC = 1
print("Can you tell what number I am thinking of?  Don't guess the same number twice ^.^")
guess = int(input("Guess a value from 1 to 100: "))
if guess < x:
    while guess < x:
        print("Yo! Too low... give it another shot")
        tryH = tryH + 1 
        guess = int(input("Guess a value from 1 to 100: "))
if guess > x:
    while guess > x:
        print("Guy, too high... go again")
        tryL = tryL + 1
        guess = int(input("Guess a value from 1 to 100: "))
if guess == x :
    print("Woohoo, you got it!", guess, "is correct")
t = tryL + tryH + tryC
print("It took you", t, "tries to get it right")