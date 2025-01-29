#Name: Ashtin Gage Huntington
#Class: 5th Hour
#Assignment: HW18

#1. Import the "random" library and create a def function that prints "Hello World!"
import random
y = 0
def hello():
    print("Hello World!!!")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["Fulvous","Zaffre","Puce","Red","Eburnean"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def eviction():

    global y
    y += 1

    if y == 5:
        print("All Beans Pulled!")
        exit()
    input("Click To Pull A Bean!!!")

    pullBean = random.choice(beanBag)
    print(f"The Color was {pullBean}!")
    beanBag.remove(pullBean)

    again()

#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def again():
    f = input("Would You Like To Pull Another Bean Y/N")
    if f == "Y" or f == "y":
        eviction()
    elif f == "N" or f == "n":
        exit()
    else:
        print("Error")
        again()



#5. Call the #3 function at the bottom.
eviction()

