#Name:
#Class: 5th Hour
#Assignment: HW24

import random
import time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.

class guy:
    def __init__(self, health, damage, speed,mhealth):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.mhealth = mhealth
    def poison(self):
        for a in range(10):
            self.health -= random.randint(1,6)
            time.sleep(1)
            print(self.health)

    def heallllll(self):
        self.health += 30
        if self.health > 100:
            self.health = 100


#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute
# values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
Warrior = guy(100,20,30,100)
Healer = guy(60, 10, 30,60)
Thief = guy(50, 30,40,50)
Mage = guy(45, 35, 25, 45)

#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
D4 = random.randint(1,4)
if D4 == 1:
    print("Warrior was Poisoned!!!")
    Warrior.poison()
if D4 == 2:
    print("Healer was Poisoned!!!")
    Healer.poison()
if D4 == 3:
    print("Thief was Poisoned!!!")
    Thief.poison()
if D4 == 4:
    print("Mage was Poisoned!!!")
    Mage.poison()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling
# your healing function to that object and then print their health afterward.
print("Healer uses heal spell!")
if not Warrior.mhealth == Warrior.health:
    Warrior.heallllll()
    print(Warrior.health)
if not Healer.mhealth == Healer.health:
    Healer.heallllll()
    print(Healer.health)
if not Thief.mhealth == Thief.health:
    Thief.heallllll()
    print(Thief.health)
if not Mage.mhealth == Mage.health:
    Mage.heallllll()
    print(Mage.health)