# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Jose", 21, "male")
print(student.count("Jose"))
print(student.index("male"))

for x in student:
    print(x)

if "Jose" in student:
    print("Jose is here!!")
