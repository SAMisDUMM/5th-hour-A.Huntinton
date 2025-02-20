#Name:Ashtin Gage Huntington
#Class: 5th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    print(100/int(input()))
except ZeroDivisionError:
    print("Can't Divide by Zero!!")
except:
    print("Failed")
#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.

try:
    g = int(input("Enter A Num!!"))
    print(g)
except ValueError:
    print("Value Error!!!")
except:
    print("Unknown Error")
#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
y = 6
while 5 == 5:
    y -= 1
    print(y)
    if y == 0:
        raise Exception("No Numbers Below Zero!!!!")

