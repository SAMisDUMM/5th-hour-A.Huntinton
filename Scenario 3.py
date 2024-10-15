#Ashting Gage Huntington
#5th Hour
#Scenario 3

print("Hello World!!!")

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4
import random

videoGame = {
    "Zombies" : {
        "AT": 4,
        "Health": 9,
        "AC":12,
        "Damage": random.randint(1, 5)},

    "Spitter" : {
        "AT": 6,
        "Health": 11,
        "AC": 13,
        "Damage": random.randint(1, 6)},

    "Runner" : {
        "AT": 7,
        "Health": 8,
        "AC": 10,
        "Damage": random.randint(1, 8)},

    "Brute" : {
        "AT": 7,
        "Health": 18,
        "AC": 16,
        "Damage": random.randint(1, 10)},

    "Mutated" : {
         "AT": 7,
        "Health": 24,
        "AC":17,
        "Damage": random.randint(1, 8)},

}
partyDict = {
    "LaeZel" : {
        "AT" : 5,
        "Health" : 16,
        "AC" : 17,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "AT": 3,
        "Health" : 24,
        "AC" : 14,
        "Damage" : random.randint(1,6) + 2
    },
    "Gale" : {
        "AT" : 4,
        "Health" : 8,
        "AC" : 10,
        "Damage" : random.randint(1,10)
    },
    "Astarion" : {
        "AT" : 6,
        "Health" : 20,
        "AC" : 14,
        "Damage" : random.randint(1,6) + 4
    }
}




print(f"LaeZel Damage:{partyDict["LaeZel"]["Damage"]}")



print(f"Shadowheart Damage:{partyDict["Shadowheart"]["Damage"]}")



print(f"Gale Damage:{partyDict["Gale"]["Damage"]}")



print(f"Astarion Damage:{partyDict["Astarion"]["Damage"]}")



AD20 = random.randint(1,20)
D20 = random.randint(1,20)
print(D20)
D4 = random.randint(1,4)

D5 = random.randint(1,5)

if D4 == 1:
    print("LaeZel is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= videoGame["Zombies"]["AC"]:
            if partyDict["LaeZel"]["Damage"] >= videoGame["Zombies"]["Health"] :
                print("Zombie Has Died ")

            else :
                print(f"Zombies Current Health :{videoGame["Zombies"]["Health"] - partyDict["LaeZel"]["Damage"]}")

                if AD20 + videoGame["Zombies"]["AT"] >= partyDict["LaeZel"]["AC"] :
                    if videoGame["Zombies"]["Damage"] >= partyDict["LaeZel"]["Health"] :
                        print("LaeZel has fainted!!!")

                    else :
                        print(f"LaeZels Current Health :{partyDict["LaeZel"]["Health"] - videoGame["Zombies"]["Damage"]}")
                else:
                    print("Zombie misses!!!")

        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= videoGame["Spitter"]["AC"]:
            if partyDict["LaeZel"]["Damage"] >= videoGame["Spitter"]["Health"]:
                print("Spitter Has Died ")

            else:
                print(f"Spitters Current Health :{videoGame["Spitter"]["Health"] - partyDict["LaeZel"]["Damage"]}")

                if AD20 + videoGame["Spitter"]["AT"] >= partyDict["LaeZel"]["AC"]:
                    if videoGame["Spitter"]["Damage"] >= partyDict["LaeZel"]["Health"]:
                        print("LaeZel has fainted!!!")

                    else:
                        print(
                            f"LaeZels Current Health :{partyDict["LaeZel"]["Health"] - videoGame["Spitter"]["Damage"]}")

                else:
                    print("Spitter misses!!!")
        else:
            print("MISS!!!")


    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= videoGame["Runner"]["AC"]:
            if partyDict["LaeZel"]["Damage"] >= videoGame["Runner"]["Health"]:
                print("Spitter Has Died ")

            else:
                print(f"Runners Current Health :{videoGame["Runner"]["Health"] - partyDict["LaeZel"]["Damage"]}")

                if AD20 + videoGame["Runner"]["AT"] >= partyDict["LaeZel"]["AC"]:
                    if videoGame["Runner"]["Damage"] >= partyDict["LaeZel"]["Health"]:
                        print("LaeZel has fainted!!!")

                    else:
                        print(
                            f"LaeZels Current Health :{partyDict["LaeZel"]["Health"] - videoGame["Runner"]["Damage"]}")

                else:
                    print("Runner misses!!!")
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= videoGame["Brute"]["AC"]:
            if partyDict["LaeZel"]["Damage"] >= videoGame["Brute"]["Health"]:
                print("Brute Has Died ")

            else:
                print(f"Brute Current Health :{videoGame["Brute"]["Health"] - partyDict["LaeZel"]["Damage"]}")

                if AD20 + videoGame["Brute"]["AT"] >= partyDict["LaeZel"]["AC"]:
                    if videoGame["Brute"]["Damage"] >= partyDict["LaeZel"]["Health"]:
                        print("LaeZel has fainted!!!")

                    else:
                        print(
                            f"LaeZels Current Health :{partyDict["LaeZel"]["Health"] - videoGame["Brute"]["Damage"]}")
                else:
                    print("Brute Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["LaeZel"]["AT"] >= videoGame["Mutated"]["AC"]:
            if partyDict["LaeZel"]["Damage"] >= videoGame["Mutated"]["Health"]:
                print("Mutated Has Died ")

            else:
                print(f"Mutated Current Health :{videoGame["Mutated"]["Health"] - partyDict["LaeZel"]["Damage"]}")

                if AD20 + videoGame["Mutated"]["AT"] >= partyDict["LaeZel"]["AC"]:
                    if videoGame["Mutated"]["Damage"] >= partyDict["LaeZel"]["Health"]:
                        print("LaeZel has fainted!!!")

                    else:
                        print(
                            f"LaeZels Current Health :{partyDict["LaeZel"]["Health"] - videoGame["Mutated"]["Damage"]}")
                else:
                    print("Mutated Misses!!!")
        else:
            print("MISS!!!")






if D4 == 2:
    print("Shadowheart is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= videoGame["Zombies"]["AC"]:
            if partyDict["Shadowheart"]["Damage"] >= videoGame["Zombies"]["Health"]:
                print("Zombies Has Died ")

            else:
                print(f"Zombies Current Health :{videoGame["Zombies"]["Health"] - partyDict["Shadowheart"]["Damage"]}")

                if AD20 + videoGame["Zombies"]["AT"] >= partyDict["Shadowheart"]["AC"]:
                    if videoGame["Zombies"]["Damage"] >= partyDict["Shadowheart"]["Health"]:
                        print("Shadowheart has fainted!!!")

                    else:
                        print(
                            f"Shadowheart Current Health :{partyDict["Shadowheart"]["Health"] - videoGame["Zombies"]["Damage"]}")
                else:
                    print("Zombies Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= videoGame["Spitter"]["AC"]:
            if partyDict["Shadowheart"]["Damage"] >= videoGame["Spitter"]["Health"]:
                print("Spitter Has Died ")

            else:
                print(f"Spitter Current Health :{videoGame["Spitter"]["Health"] - partyDict["Shadowheart"]["Damage"]}")

                if AD20 + videoGame["Spitter"]["AT"] >= partyDict["Shadowheart"]["AC"]:
                    if videoGame["Spitter"]["Damage"] >= partyDict["Shadowheart"]["Health"]:
                        print("Shadowheart has fainted!!!")

                    else:
                        print(
                            f"Shadowheart Current Health :{partyDict["Shadowheart"]["Health"] - videoGame["Spitter"]["Damage"]}")
                else:
                    print("Spitter Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= videoGame["Runner"]["AC"]:
            if partyDict["Shadowheart"]["Damage"] >= videoGame["Runner"]["Health"]:
                print("Runner Has Died ")

            else:
                print(f"Runner Current Health :{videoGame["Runner"]["Health"] - partyDict["Shadowheart"]["Damage"]}")

                if AD20 + videoGame["Runner"]["AT"] >= partyDict["Shadowheart"]["AC"]:
                    if videoGame["Runner"]["Damage"] >= partyDict["Shadowheart"]["Health"]:
                        print("Shadowheart has fainted!!!")

                    else:
                        print( f"Shadowheart Current Health :{partyDict["Shadowheart"]["Health"] - videoGame["Runner"]["Damage"]}")
                else:
                    print("Runner Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= videoGame["Brute"]["AC"]:
            if partyDict["Shadowheart"]["Damage"] >= videoGame["Brute"]["Health"]:
                print("Spitter Has Died ")

            else:
                print(f"Brute Current Health :{videoGame["Brute"]["Health"] - partyDict["Shadowheart"]["Damage"]}")

                if AD20 + videoGame["Brute"]["AT"] >= partyDict["Shadowheart"]["AC"]:
                    if videoGame["Brute"]["Damage"] >= partyDict["Shadowheart"]["Health"]:
                        print("Shadowheart has fainted!!!")

                    else:
                        print(f"Shadowheart Current Health :{partyDict["Shadowheart"]["Health"] - videoGame["Brute"]["Damage"]}")
                else:
                    print("Brute Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= videoGame["Mutated"]["AC"]:
            if partyDict["Shadowheart"]["Damage"] >= videoGame["Mutated"]["Health"]:
                print("Mutated Has Died ")

            else:
                print(f"Mutated Current Health :{videoGame["Mutated"]["Health"] - partyDict["Shadowheart"]["Damage"]}")

                if AD20 + videoGame["Mutated"]["AT"] >= partyDict["Shadowheart"]["AC"]:
                    if videoGame["Mutated"]["Damage"] >= partyDict["Shadowheart"]["Health"]:
                        print("Shadowheart has fainted!!!")

                    else:
                        print(f"Shadowheart Current Health :{partyDict["Shadowheart"]["Health"] - videoGame["Mutated"]["Damage"]}")
                else:
                    print("Mutated Misses!!!")
        else:
            print("MISS!!!")
###
if D4 == 3:
    print("Gale is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["Gale"]["AT"] >= videoGame["Zombies"]["AC"]:
            if partyDict["Gale"]["Damage"] >= videoGame["Zombies"]["Health"]:
                print("Zombies Has Died ")

            else:
                print(f"Zombies Current Health :{videoGame["Zombies"]["Health"] - partyDict["Gale"]["Damage"]}")

                if AD20 + videoGame["Zombies"]["AT"] >= partyDict["Gale"]["AC"]:
                    if videoGame["Zombies"]["Damage"] >= partyDict["Gale"]["Health"]:
                        print("Gale has fainted!!!")

                    else:
                        print(f"Gale Current Health :{partyDict["Gale"]["Health"] - videoGame["Zombies"]["Damage"]}")
                else:
                    print("Zombies Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["Gale"]["AT"] >= videoGame["Spitter"]["AC"]:
            if partyDict["Gale"]["Damage"] >= videoGame["Spitter"]["Health"]:
                print("Spitter Has Died ")

            else:
                print(f"Spitter Current Health :{videoGame["Spitter"]["Health"] - partyDict["Gale"]["Damage"]}")

                if AD20 + videoGame["Spitter"]["AT"] >= partyDict["Gale"]["AC"]:
                    if videoGame["Spitter"]["Damage"] >= partyDict["Gale"]["Health"]:
                        print("Gale has fainted!!!")

                    else:
                        print(
                            f"Gale Current Health :{partyDict["Gale"]["Health"] - videoGame["Spitter"]["Damage"]}")
                else:
                    print("Spitter Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["Gale"]["AT"] >= videoGame["Runner"]["AC"]:
            if partyDict["Gale"]["Damage"] >= videoGame["Runner"]["Health"]:
                print("Runner Has Died ")

            else:
                print(f"Runner Current Health :{videoGame["Runner"]["Health"] - partyDict["Gale"]["Damage"]}")

                if AD20 + videoGame["Runner"]["AT"] >= partyDict["Gale"]["AC"]:
                    if videoGame["Runner"]["Damage"] >= partyDict["Gale"]["Health"]:
                        print("Gale has fainted!!!")

                    else:
                        print(
                            f"Gale Current Health :{partyDict["Gale"]["Health"] - videoGame["Runner"]["Damage"]}")
                else:
                    print("Runner Misses!!!")

        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["Gale"]["AT"] >= videoGame["Brute"]["AC"]:
            if partyDict["Gale"]["Damage"] >= videoGame["Brute"]["Health"]:
                print("Brute Has Died ")

            else:
                print(f"Brute Current Health :{videoGame["Brute"]["Health"] - partyDict["Gale"]["Damage"]}")

                if AD20 + videoGame["Brute"]["AT"] >= partyDict["Gale"]["AC"]:
                    if videoGame["Brute"]["Damage"] >= partyDict["Gale"]["Health"]:
                        print("Gale has fainted!!!")

                    else:
                        print(
                            f"Gale Current Health :{partyDict["Gale"]["Health"] - videoGame["Brute"]["Damage"]}")
                else:
                    print("Brute Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["Gale"]["AT"] >= videoGame["Mutated"]["AC"]:
            if partyDict["Gale"]["Damage"] >= videoGame["Mutated"]["Health"]:
                print("Mutated Has Died ")

            else:
                print(f"Mutated Current Health :{videoGame["Mutated"]["Health"] - partyDict["Gale"]["Damage"]}")

                if AD20 + videoGame["Mutated"]["AT"] >= partyDict["Gale"]["AC"]:
                    if videoGame["Mutated"]["Damage"] >= partyDict["Gale"]["Health"]:
                        print("Gale has fainted!!!")

                    else:
                        print(
                            f"Gale Current Health :{partyDict["Gale"]["Health"] - videoGame["Mutated"]["Damage"]}")
                else:
                    print("Mutated Misses!!!")
        else:
            print("MISS!!!")





if D4 == 4:
    print("Astarion is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["Astarion"]["AT"] >= videoGame["Zombies"]["AC"]:
            if partyDict["Astarion"]["Damage"] >= videoGame["Zombies"]["Health"]:
                print("Zombies Has Died ")

            else:
                print(f"Zombies Current Health :{videoGame["Zombies"]["Health"] - partyDict["Astarion"]["Damage"]}")

                if AD20 + videoGame["Zombies"]["AT"] >= partyDict["Astarion"]["AC"]:
                    if videoGame["Zombies"]["Damage"] >= partyDict["Astarion"]["Health"]:
                        print("Astarion has fainted!!!")

                    else:
                        print(
                            f"Astarion Current Health :{partyDict["Astarion"]["Health"] - videoGame["Zombies"]["Damage"]}")
                else:
                    print("Zombies Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["Astarion"]["AT"] >= videoGame["Spitter"]["AC"]:
            if partyDict["Astarion"]["Damage"] >= videoGame["Spitter"]["Health"]:
                print("Spitter Has Died ")

            else:
                print(f"Spitter Current Health :{videoGame["Spitter"]["Health"] - partyDict["Astarion"]["Damage"]}")

                if AD20 + videoGame["Spitter"]["AT"] >= partyDict["Astarion"]["AC"]:
                    if videoGame["Spitter"]["Damage"] >= partyDict["Astarion"]["Health"]:
                        print("Astarion has fainted!!!")

                    else:
                        print(
                            f"Astarion Current Health :{partyDict["Astarion"]["Health"] - videoGame["Spitter"]["Damage"]}")
                else:
                    print("Spitter Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["Astarion"]["AT"] >= videoGame["Runner"]["AC"]:
            if partyDict["Astarion"]["Damage"] >= videoGame["Runner"]["Health"]:
                print("Runner Has Died ")

            else:
                print(f"Runner Current Health :{videoGame["Runner"]["Health"] - partyDict["Astarion"]["Damage"]}")

                if AD20 + videoGame["Runner"]["AT"] >= partyDict["Astarion"]["AC"]:
                    if videoGame["Runner"]["Damage"] >= partyDict["Astarion"]["Health"]:
                        print("Astarion has fainted!!!")

                    else:
                        print(
                            f"Astarion Current Health :{partyDict["Astarion"]["Health"] - videoGame["Runner"]["Damage"]}")
                else:
                    print("Runner Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["Astarion"]["AT"] >= videoGame["Brute"]["AC"]:
            if partyDict["Astarion"]["Damage"] >= videoGame["Brute"]["Health"]:
                print("Brute Has Died ")

            else:
                print(f"Brute Current Health :{videoGame["Brute"]["Health"] - partyDict["Astarion"]["Damage"]}")

                if AD20 + videoGame["Brute"]["AT"] >= partyDict["Astarion"]["AC"]:
                    if videoGame["Brute"]["Damage"] >= partyDict["Astarion"]["Health"]:
                        print("Astarion has fainted!!!")

                    else:
                        print(
                            f"Astarion Current Health :{partyDict["Astarion"]["Health"] - videoGame["Brute"]["Damage"]}")
                else:
                    print("Brute Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["Astarion"]["AT"] >= videoGame["Mutated"]["AC"]:
            if partyDict["Astarion"]["Damage"] >= videoGame["Mutated"]["Health"]:
                print("Mutated Has Died ")

            else:
                print(f"Mutated Current Health :{videoGame["Mutated"]["Health"] - partyDict["Astarion"]["Damage"]}")

                if AD20 + videoGame["Mutated"]["AT"] >= partyDict["Astarion"]["AC"]:
                    if videoGame["Mutated"]["Damage"] >= partyDict["Astarion"]["Health"]:
                        print("Astarion has fainted!!!")

                    else:
                        print(
                            f"Astarion Current Health :{partyDict["Astarion"]["Health"] - videoGame["Mutated"]["Damage"]}")
                else:
                    print("Mutated Misses!!!")
        else:
            print("MISS!!!")















