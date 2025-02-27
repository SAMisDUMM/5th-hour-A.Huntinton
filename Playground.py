#Ashtin Gage Huntington
#5th Hour Class
#Playground
import random
y = 0
money = 32
print("Welcome To Stonks")
print("How to PLay- You Begin With 32$. Hit Enter To Gamble,N/n to End.It Could Half Or Double Your Money. If You Get An Odd Numba You  Own Me Dolla, Make The Most Money!!!")

def game():
    global money
    global y
    x = random.randint(1,2)
    y += 1
    print(f"You Have {money}$")
    hah = input(":")
    if hah == "n" or hah == "N":

        print(f"You Won {money}")

    else:

        if x == 1:
            money /= 2
            print("Negative!")
            if money < 1:
                print("Game Over")
                exit()
            else:
                game()
        if x == 2:
            money *= 2
            print("Double!!")
            game()

















game()

