#Ashtin Gage Huntington
#5th Hour Class
#Playground
print("Hello, Welcome to Grocery List AI" )
x = input("Please ENTER name here: ")
print(f"Welcome {x} to Grocery List AI")
print("Your current List Includes the Following")
GroceryList =["Eggs","Milk","Pancakes","Dough","Human Child from Streets"]
print(GroceryList)
print("What Items would you Like to add to You List?")
GroceryList.append(input())
print(GroceryList)
print("Would you like to Continue or Exit Grocery List AI?")
print("If you Want Continue, Type 1")
print("If you Want to Exit, Type 2")
y = int(input())
if y == 1:
    print("What Items would you Like to add to You List?")
    GroceryList.append(input())
    print(GroceryList)
    print("Would you like to Continue or Exit Grocery List AI?")
    print("If you Want Continue, Type 1")
    print("If you Want to Exit, Type 2")
    a = int(input())
    if a == 1:
        print("What Items would you Like to add to You List?")
        GroceryList.append(input())
        print(GroceryList)
        print("Would you like to Continue or Exit Grocery List AI?")
        print("If you Want Continue, Type 1")
        print("If you Want to Exit, Type 2")
        b = int(input())
        if b == 1:
            print("What Items would you Like to add to You List?")
            GroceryList.append(input())
            print(GroceryList)
            print("ERROR WIFI RESOLUTION ISSUE")
            print("GROCERY LIST AI SHUT IN 5")
            print("4")
            print("3")
            print("2")
            print("1")
            print("Now Exiting...")
        elif b == 2:
            print("Bye")

    elif a == 2:
        print("Bye")

elif y == 2:
    print("Bye")
