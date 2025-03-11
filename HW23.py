#Name:
#Class: 5th Hour
#Assignment: HW23

#1. Import the random and time libraries
import random
import time
#2. Create a class containing a def function that inits self and the 3 attributes health, damage, and speed.
class guy:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def loooooop(self):
        for a in range(10):
            Warrior.health -= random.randint(1,6)
            time.sleep(1)
            print(Warrior.health)

    def heallllll(self):
        Warrior.health += 30
        if Warrior.health > 100:
            Warrior.health = 100
#3. Make a "warrior" character object with 100 health, 20 damage, and 30 speed. Print the character's initial health below.
Warrior = guy(100,20,30)
print(Warrior.health)
#4. Make a def function within the class that loops 10 times. Within this function,
#make the following loop 10 times: the character takes a random amount of damage from 1 to 6,
#the new health is printed, a time.sleep delay of one second is done. Call the function to the warrior.
Warrior.loooooop()
#5. Make a "healer" character object with 60 health, 10 damage, and 30 speed.
Healer = guy(60, 10, 30)
#6. Make a def function within the class that heals the warrior for 30 health. Create an if statement
#that sets the warrior's health to its max (100) if the healing would bring the warrior's health above that.
#Call the function to the healer.
Healer.heallllll()

print(Warrior.health)