#Ashting Gage Huntington
#5th Hour
#HW13

#1. Create a list containing 10 integers of your choice.

list1 = [6,9,69,96,66,99,969,696,669,996]

#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0

oddNumbers = 0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).


for i in list1:
    if i %2 == 0:
        evenNumbers+=1

    else:
        oddNumbers+=1





# Print the total count of even and odd numbers.
print(evenNumbers)

print(oddNumbers)