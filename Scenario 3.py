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

#Roll1 = [random.randint(1,6)]


print(f"LaeZel Damage:{partyDict["LaeZel"]["Damage"]+partyDict["LaeZel"]["Damage"]+partyDict["LaeZel"]["Damage"]}")



print(f"Shadowheart Damage:{partyDict["Shadowheart"]["Damage"]+partyDict["Shadowheart"]["Damage"]}")



print(f"Gale Damage:{partyDict["Gale"]["Damage"]}")



print(f"Astarion Damage:{partyDict["Astarion"]["Damage"]+partyDict["Astarion"]["Damage"]}")




D20 = random.randint(1,20)
print(D20)
D4 = random.randint(1,4)

D5 = random.randint(1,5)

if D4 == 1:
    print("LaeZel is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= partyDict["Zombies"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= partyDict["Spitter"]["AC"]:
            pass
        else:
            print("MISS!!!")


    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= partyDict["Runner"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["LaeZel"]["AT"] >= partyDict["Brute"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["LaeZel"]["AT"] >= partyDict["Mutated"]["AC"]:
            pass
        else:
            print("MISS!!!")






if D4 == 2:
    print("Shadowheart is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= partyDict["Zombies"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= partyDict["Spitter"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= partyDict["Runner"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= partyDict["Brute"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["Shadowheart"]["AT"] >= partyDict["Mutated"]["AC"]:
            pass
        else:
            print("MISS!!!")

if D4 == 3:
    print("Gale is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["Gale"]["AT"] >= partyDict["Zombies"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["Gale"]["AT"] >= partyDict["Spitter"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["Gale"]["AT"] >= partyDict["Runner"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["Gale"]["AT"] >= partyDict["Brute"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["Gale"]["AT"] >= partyDict["Mutated"]["AC"]:
            pass
        else:
            print("MISS!!!")





if D4 == 4:
    print("Astarion is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + partyDict["Astarion"]["AT"] >= partyDict["Zombies"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + partyDict["Astarion"]["AT"] >= partyDict["Spitter"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 3:
        print("Runner!!!")

        if D20 + partyDict["Astarion"]["AT"] >= partyDict["Runner"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + partyDict["Astarion"]["AT"] >= partyDict["Brute"]["AC"]:
            pass
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + partyDict["Astarion"]["AT"] >= partyDict["Mutated"]["AC"]:
            pass
        else:
            print("MISS!!!")















