#Ashting Gage Huntington
#5th Hour
#Scenario 4


#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all the ratings.



import random
print("Hello World!!!")
i = 0
t = 0
y = 0
j = 0

print("Welcome To Project Dress-Up!!!!")

input("Press Anything To Enter: ")

x = int(input("Please Enter Number Of Players: "))

a = x - 1

print(f"You Have Selected {x} Players!!")

while not a == x:


    gender = random.randint(1, 4)
    dress = random.randint(1, 6)
    shoes = random.randint(1, 4)
    ac = random.randint(1, 8)


    print("A New Contender Has Entered The Stage!!")
    print("The Subject Is A...")

    if gender == 1:
        print("Luxurious Female!")

    if gender == 2:
        print("Short Woman")

    if gender == 3:
        print("Muscular Adult Male")

    if gender == 4:
        print("Robot?")

    print("Wearing A....")

    if dress == 1:
        print("Silky Red Dress.")

    if dress == 2:
        print("Blow-Up Cheese Costume.")

    if dress == 3:
        print("Butterfly Costume.")

    if dress == 4:
        print("Gigantic Walmart Sack.")

    if dress == 5:
        print("Formal Cloths.")

    if dress == 6:
        print("Fine, Dashing Clothing.")

    print("With Shoes Of...")

    if shoes == 1:
        print("Gold!?!?")

    if shoes == 2:
        print("Red, Beautiful Heels")

    if shoes == 3:
        print("Cheese")

    if shoes == 4:
        print("Nothing? They're Barefoot....")

    print("They Entered With...")

    if ac == 1:
        print("A Golden Necklace Around Their neck")

    if ac == 2:
        print("A Canned Beans?")

    if ac == 3:
        print("A Pet Rock ")

    if ac == 4:
        print("A Flaming, Ruby Ring")

    if ac == 5:
        print("A Rose")

    if ac == 6:
        print("A Cheese Basket")

    if ac == 7:
        print("A Robo Dog")

    if ac == 8:
        print("Nothing..?")

    while not j == x:
        i = int(input("Enter Rating: "))

        while i > 5 or i < 1:
            print("Try again")
            i = int(input("Enter Corrected Rating: "))
            if i < 6 and i > 0:
                break
            else:
                continue
        j += 1



    print("GAME-OVER!!")





    g = i / x

    print(f"Your Average Rating Was {g}")



    a += 1



#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all the ratings.