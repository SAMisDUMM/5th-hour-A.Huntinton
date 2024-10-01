#Ashting Gage Huntington
#5th Hour
#HW6

print("Hello World!!!")

num = int(input("Number 1 : "))


if num%2 == 0 or num%3 == 0:
    if num % 3 == 0:
        print(f"{num} is Divisible by 3")
        print(f"{num}/3 = {num / 3}")
        if num%3==0 and num%2==0:
            print(f"{num} is divisible by 2")
            print(f"{num}/2 = {num / 2}")
            exit()
        else:
            print(f"{num} is NOT divisible by 2")



    if num % 2 == 0:
        print(f"{num} is divisible by 2")
        print(f"{num}/2 = {num / 2}")

        if num%3==0 and num%2==0:
            print(f"{num} is divisible by 3")
            print(f"{num}/3 = {num / 3}")
            exit()
        else:
            print(f"{num} is NOT divisible by 3")






else:
    print(f"{num} is not divisible by neither 2 nor 3")

