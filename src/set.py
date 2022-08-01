# set =  collection which is unordered, unindexed. No duplicates values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

# Adding an element to the set
utensils.add("napkin")
print("Set: ", utensils)

utensils.remove("napkin")
print("Set: ", utensils)

utensils.update(dishes)
print("Set: ", utensils)

dinner_table = utensils.union(dishes)
print("Set dinner_table: ", dinner_table)

# Checking differences
dishes.add("knife")
print("Differences between dishes and utensils", utensils.difference(dishes))

# Checking intersection
print("Intersection  between dishes and utensils", utensils.intersection(dishes))

for x in utensils:
    print(x)
