# slicing: create a substring by extracting elements from another string
#          indexing[] or slice()
#          [start:stop:step]

name = "Jose Javier Blecua"

first_name = name[:11]
last_name = name[12:]
funky_name = name[::2]
reversed_name = name[::-1]

print("First name: " + first_name)
print("Last name: " + last_name)
print("Funky name: " + funky_name)
print("Reversed name: " + reversed_name)

# Slicing function
website = "http://google.com"
wiki_website = "http://wikipedia.com"

slice = slice(7, -4)
print("Website name1: ", website[slice])
print("Website name2: ", wiki_website[slice])
