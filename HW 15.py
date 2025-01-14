#Name: Ashtin Gage Huntington
#Class: 5th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"

def hello_world():
    print("Hello World")

#2. Create a def function that calculates the average of three numbers.

def average(a,b,c):
    d = a+b+c
    print(d/3)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.

def animals(*animal):
    print("The Third Animal is", animal[2])

#4. Create a def function that loops from 1 to the number put in the argument.

def looooop(g = int(input("Input Num Here: "))):
    h = 0
    while not h == g:
        h+=1
        print(h)
    else:
        exit()

#5. Call all of the functions created in 1 - 4 with relevant arguments.

hello_world()
average(6,10,2)
animals("Zebra", "Gorilla", "Dog","Camel Raymond","Me")
looooop(int(input("Input Num Here: ")))