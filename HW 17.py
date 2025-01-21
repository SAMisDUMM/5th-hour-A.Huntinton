#Name: Ashtin H.
#Class: 5th Hour
#Assignment: HW17





#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello_world():
    print("Hello World!")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def flip():
    x=0

    global heads
    global tails

    while not x == 100:
        coin = random.randint(1, 2)
        if coin == 1:
            heads += 1
            print("Heads!")
            x+=1

        if coin == 2:
            tails += 1
            print("Tails!")
            x+=1
    print(f"Tails was Flipped {tails} Times,"
          f" While Heads was FLipped {heads} Times")



#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
flip()

