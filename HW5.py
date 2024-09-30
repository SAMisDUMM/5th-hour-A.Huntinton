#Ashting Gage Huntington
#5th Hour
#HW5

print("Hello World!!!")

a = int(input("Number 1 : "))
b = int(input("Number 2 : "))
c = int(input("Number 3 : "))



Unicorn = (a, b, c )
print(Unicorn)
if a > b and a > c:
    print(f"Number 1 ({a}) is the Greatest Number.")
if b > a and b > c:
    print(f"Number 2 ({b}) is the Greatest Number.")
if c > a and c > b:
    print(f"Number 3 ({c}) is the Greatest Number.")
if b == a:
    print(f"Number 2 ({b}) Equals Number 1 ({a})")
if c == a:
    print(f"Number 3 ({c}) Equals Number 1 ({a})")
if b == c :
    print(f"Number 2 ({b}) Equals Number 3 ({c})")
if b == a and a == c:
    print("All Numbers are Equal")


