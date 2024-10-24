#Ashting Gage Huntington
#5th Hour
#HW9

import random

Temp = random.randint(0,30)

if Temp > 20:
    print("Its Hot")
    print("Thank You")
else:
    if Temp > 10:
        print("Its Mild")
        print("Thank You")
    else:
        print("Its Cold")
        print("Thank You")