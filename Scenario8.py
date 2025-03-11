#Name:Ashtin Gage Huntington
#Class: 5th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

class S3:
    def __init__(self, Health, AT, Damage, AC):
        self.AT = AT
        self.Health = Health
        self.Damage = Damage
        self.AC = AC

LaeZel = S3(23,3,random.randint(4,15),11)
Shadowheart = S3(12,4,random.randint(3,8),10)
Gale = S3(19,3,random.randint(1,10),15)
Astarion = S3(20,4,random.randint(5,11),15)

Zombies = S3(9,4,random.randint(1, 5),12)
Spitter = S3(11,6,random.randint(1, 6),13)
Runner = S3(8,7,random.randint(1, 8),10)
Brute = S3(18,7,random.randint(1, 12),16)
Mutated = S3(24,17,random.randint(1, 10),17)

AD20 = random.randint(1,20)
D20 = random.randint(1,20)
print(D20)
D4 = random.randint(1,1)

D5 = random.randint(1,5)

if D4 == 1:
    print("LaeZel is attacking...")

    if D5 == 1:
        print("Zombies!!!")

        if D20 + LaeZel.AT >= Zombies.AC :
            if LaeZel.Damage >= Zombies.Health :
                print("Zombie Has Died ")

            else :
                print(f"Zombies Current Health :{Zombies.Health - LaeZel.Damage}")

                if AD20 + Zombies.AT >= LaeZel.AC :
                    if Zombies.Damage >= LaeZel.Health :
                        print("LaeZel has fainted!!!")

                    else :
                        print(f"LaeZel's Current Health :{LaeZel.Health - Zombies.Damage}")
                else:
                    print("Zombie misses!!!")

        else:
            print("MISS!!!")

    if D5 == 2:
        print("Spitter!!!")

        if D20 + LaeZel.AT >= Spitter.AC:
            if LaeZel.Damage >= Spitter.Health:
                print("Spitter Has Died ")

            else:
                print(f"Spitter's Current Health :{Spitter.Health - LaeZel.Damage}")

                if AD20 + Spitter.AT >= LaeZel.AC:
                    if Spitter.Damage >= LaeZel.Health:
                        print("LaeZel has fainted!!!")

                    else:
                        print(f"LaeZel's Current Health :{LaeZel.Health - Spitter.Damage}")

                else:
                    print("Spitter misses!!!")
        else:
            print("MISS!!!")


    if D5 == 3:
        print("Runner!!!")

        if D20 + LaeZel.AT >= Runner.AC:
            if LaeZel.Damage >= Runner.Health:
                print("Runner Has Died ")

            else:
                print(f"Runners Current Health :{Runner.Health - LaeZel.Damage}")

                if AD20 + Runner.AT >= LaeZel.AC:
                    if Runner.Damage>= LaeZel.Health:
                        print("LaeZel has fainted!!!")

                    else:
                        print(
                            f"LaeZel's Current Health :{LaeZel.Health - Runner.Damage}")

                else:
                    print("Runner misses!!!")
        else:
            print("MISS!!!")

    if D5 == 4:
        print("Brute!!!")

        if D20 + LaeZel.AT >= Brute.AC:
            if LaeZel.Damage >= Brute.Health:
                print("Brute Has Died ")

            else:
                print(f"Brute Current Health :{Brute.Health - LaeZel.Damage}")

                if AD20 + Brute.AT >= LaeZel.AC:
                    if Brute.Damage >= LaeZel.Health:
                        print("LaeZel has fainted!!!")

                    else:
                        print(
                            f"LaeZel's Current Health :{LaeZel.Health - Brute.Damage}")
                else:
                    print("Brute Misses!!!")
        else:
            print("MISS!!!")

    if D5 == 5:
        print("Mutated??!!")

        if D20 + LaeZel.AT >= Mutated.AC:
            if LaeZel.Damage >= Mutated.Health:
                print("Mutated Has Died ")

            else:
                print(f"Mutated Current Health :{Mutated.Health - LaeZel.Damage}")

                if AD20 + Mutated.AT >= LaeZel.AC:
                    if Mutated.Damage >= LaeZel.Health:
                        print("LaeZel has fainted!!!")

                    else:
                        print(
                            f"LaeZel's Current Health :{LaeZel.Health - Mutated.Damage}")
                else:
                    print("Mutated Misses!!!")
        else:
            print("MISS!!!")