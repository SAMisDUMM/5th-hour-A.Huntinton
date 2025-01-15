#Name:
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

r = 1
p = 2
s = 3
def rps():
    player = int(input("RPS?  :"))
    enemy = random.randint(1, 3)
    if player == 1:
        print("Player Used Rock")
    if player == 2:
        print("Player Used Paper")
    if player == 3:
        print("Player Used Scissors")
    if enemy == 1:
        print("Enemy Used Rock")
    if enemy == 2:
        print("Enemy Used Paper")
    if enemy == 3:
        print("Enemy Used Scissors")
    if enemy == player:
        print ("The Game Was A Tie!")
    if player == 1 and enemy == 2:
        print("You've Lost!")
    if player == 2 and enemy == 3:
        print("You've Lost!")
    if player == 3 and enemy == 1:
        print("You've Lost!")
    if player == 1 and enemy == 3 :
        print("You Won!")
    if player == 2 and enemy == 1 :
        print("You Won!")
    if player == 3 and enemy == 2 :
        print("You Won!")

    h = int(input("Would You Like To Play Again? Yes = 10 No = Anything Else  :"))
    if h == 10:
        rps()

    else:
        exit()


rps()





