#Ashtin Gage Huntington
#5th Hour Class
#Playground
import random
import time

A = random.randint(1,20)
B = random.randint(1,20)
C = random.randint(1,20)

time.sleep(1)
print("You're alone... in a dark room..ROLL PERCEPTION")
print(f"You roll a {A}!")
print(A)
if A < 10 and A > 1:
    print("You see a jail door, with no way out...")
    print("What do you do?")
    print("1) Cough...")
    print("2) Search Area")
    print("3) Roll Luck")
    Inn = input(":")
    if Inn == 1:
        print("You Got the plague...YOU'RE DEAD!!!")

    if Inn == 2:
        print("ROLL FOR IT!!!")
        print("You roll a...")
        print(B)

    if Inn == 3:
        print("ROLL FOR IT!!!")
        print("You roll a...")
        print(B)

        if B == 20:
            print("You turn into god, breaking the entire prison and escaping... YOU WIN!!!")


if A > 10:
    print("You see a metal jail door, and a sleeping guard with a KEY!!!")
    print("What do you do?")
    print("A) Steal Key")
    print("B) Cry Loudly")


if A == 1:
    print("You die from a cough...")
    print("GAME OVER")
    exit()

