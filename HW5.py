#Ashting Gage Huntington
#5th Hour
#HW5

print("Hello World!!!")

numList = [5, 6, 6]




print(numList)
if numList[0] > numList[1] and numList[0] > numList[2]:
    print(f"Number 1 ({numList[0]}) is the Greatest Number.")
if numList[1] > numList[0] and numList[1] > numList[2]:
    print(f"Number 2 ({numList[1]}) is the Greatest Number.")
if numList[2] > numList[0] and numList[2] > numList[1]:
    print(f"Number 3 ({numList[2]}) is the Greatest Number.")
if numList[1] == numList[0]:
    print(f"Number 2 ({numList[1]}) Equals Number 1 ({numList[0]})")
if numList[2] == numList[0]:
    print(f"Number 3 ({numList[2]}) Equals Number 1 ({numList[0]})")
if numList[1] == numList[2] :
    print(f"Number 2 ({numList[1]}) Equals Number 3 ({numList[2]})")
if numList[1] == numList[0] and numList[0] == numList[2]:
    print("All Numbers are Equal")


