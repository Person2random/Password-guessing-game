import random


print("Your random number is between the range of 0-10000")

inte = random.randint(0,10000)

while True:
    guess = input("Whats the number you guesed? ")

    if guess == "i give up":
        print(inte)
        break
    if int(guess) == inte:
        print("You're correct!")
        break
    if int(guess) != inte:
        if int(guess) > inte:
            print("You guessed high")
        else:
            print("You guessed low")
