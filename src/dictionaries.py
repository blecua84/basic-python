# dictionary = A changeable, unordered collection of unique key:value pairs.
#              Fast because they use hashing, allow us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "Spain": "Madrid",
            "Russia": "Moscow"}
print("###########################################")
# print(capitals["Russia"])
# print(capitals["Germany"]) -> Not exist. KeyError
# print(capitals.get("Germany")) -> Value or None
# print(capitals.values())
# print(capitals.items())

# Immutable once the program is running
capitals.update({"Germany": "Berlin"})
for key, value in capitals.items():
    print(key, value)
print("###########################################")

capitals.update({"USA": "Las Vegas"})
for key, value in capitals.items():
    print(key, value)
print("###########################################")

capitals.pop("Russia")
for key, value in capitals.items():
    print(key, value)
print("###########################################")

capitals.clear()
print("Items: {}", capitals.items())
print("###########################################")
