import random
number=random.randint(1,100)
attempts=0
mattempts=5
print("Welcome to Guess Game!")
print("\n Guess a number between 1 and 100 in 5 attempts\n")
while attempts<=mattempts:
    guess=int(input("Enter your guess: "))
    attempts=attempts+1
    if(guess==number):
        print(f"Congratulations! You guessed it in {attempts} attempts")
        break
    elif(guess>number):
        print("Too high! Try again")
    else:
        print("Too low! Try again")

if(guess!=number):
    print("You lost... The number was",number)


