# list = used to store multiple items in a single variable

food = ["pizza", "fries", "hamburger", "hotdog", "spaghetti"]
# Print all elements
# print(food)

# Access to an element in the list using its index. IndexError will be thrown if there is no value for the index
print(food[0])

for x in food:
    print(x)
print()

#  Util functions
food.append("Ice scream")
print("Final list: ", food)

# Remove a type of food
food.remove("fries")
print("List with no fries: ", food)

# Remove last element
food.pop()
print("Remove last element: ", food)

# Insert new type of food in the first position
food.insert(0, "cake")
print("New List with cake", food)

# Sort the list in alphabetical order
food.sort()
print("Sorted list: ", food)

# Remove all the elements of the list
food.clear()
print("Cleared list: ", food)
