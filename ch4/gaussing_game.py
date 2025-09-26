import random

number = random.randint(1, 10)
print(number)
while True:
    guess = int(input("Guess a number between 1 and 10 (0 to quit): "))
    if guess == 0:
        print("Thanks for playing!")
        break
    elif guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
