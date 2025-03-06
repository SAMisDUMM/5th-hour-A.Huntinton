#Name:
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store:
    def __init__(self, amount, cost, weight):
        self.amount = amount
        self.cost = cost
        self.weight = weight
    def double_cost(self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
cheese_wheel=Store(5, 20, 15)
ham=Store(17, 32, 15)
hippopotamus_plush=Store(8, 22, 4)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"Cheese Wheel Stock : {cheese_wheel.amount}")
print(f"Ham Stock : {ham.amount}")
print(f"Hippopotamus Plush Stock : {hippopotamus_plush.amount}")
print(f"Cheese Wheel Costs : {cheese_wheel.cost}")
print(f"Ham Costs : {ham.cost}")
print(f"Hippopotamus Plush Costs : {hippopotamus_plush.cost}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new
# cost below the original cost print statement.
ham.double_cost()
print(f"New Ham Costs : {ham.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
hippopotamus_plush.amount = 2
print(f"New Hippopotamus Plush Stock: {hippopotamus_plush.amount}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del cheese_wheel
try: print(f"Cheese Wheel Weight: {cheese_wheel.weight}")

except NameError:
    print("Error Item Deleted")

except:
    print("New Error")