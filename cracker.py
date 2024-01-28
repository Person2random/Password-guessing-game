import random

roof = 10000
floor = 0
guess = random.randint(0,10000)
already = []













while True:
    print(guess)
    tre = input("high or low or correct? \n")
    if tre.lower() == "high":
        roof = guess
        already.append(guess)
    if tre.lower() == "low":
        floor = guess
        already.append(guess)
    if tre.lower() == "correct":
        break
    print(f"The number will be between {floor} and {roof}")
    guess = random.randint(floor +1 ,roof -1)


