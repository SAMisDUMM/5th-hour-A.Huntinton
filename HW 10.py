#Ashting Gage Huntington
#5th Hour
#HW10
import time


#Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.

i = 5
while i > 0:
    print(i)
    time.sleep(1)
    i -= 1

else:
    print("Hello World!")



#2. Create a while loop that prints only even numbers
#between 1 and 30.


a = 2
while a <= 30:
    print(a)
    time.sleep(0.25)
    a += 2
else:
    pass



#3. Create a while loop that repeats until the user
#inputs the number 0.


b = 1
while not b == 0:
    print("Press 0 To Enter")
    b = int(input(":"))
    if b == 0:
        print("You may Enter")
        break

    else:
        print("Incorrect, Try Agin!!!")



