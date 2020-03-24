import random
import time

die1 = 0
die2 = 0

roll_again = "yes"

while roll_again == "yes":
    die1 = random.randint(1,7)
    die2 = random.randint(1,7)

    print("Rolling the dice...")
    time.sleep(2)

    print("The first die rolled a:", die1)
    time.sleep(3)
    print("The second die rolld a:", die2)
    time.sleep(1)
    if die1 > die2:
        print("Die #1 is greater than Die #2")
    elif die1 == die2:
        print("Both die have the same value")
    else:
        print("Die #2 is greater than Die #1")

    time.sleep(1.5)
    roll_again = input("Would you like to roll again?").lower()
    if roll_again.lower() != "yes":
        break
    print("---------------------------------------------------------")