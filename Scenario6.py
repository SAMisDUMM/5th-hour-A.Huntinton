#Name:
#Class: 5th Hour
#Assigment: Scenario 6
import random

#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.

#Once that is done, to ensure that the average of the stat-block is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (Scenario 7) and print the average.

def stats():

    y = 0
    while not y == 6:
        aD6 = random.randint(1, 6)
        bD6 = random.randint(1, 6)
        cD6 = random.randint(1, 6)
        dD6 = random.randint(1, 6)

        y += 1

        Dice = [aD6, bD6, cD6, dD6]
        Dice.remove(min(Dice))
        print(Dice)
        num = sum(Dice)
        print(sum(Dice))
        final.append(num)
    print(final)

final = []


stats()





