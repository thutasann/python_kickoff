print("--------------- INDEXING ---------------- ")

# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "thuta Sann"

if (name[0].lower()):
    name = name.capitalize()

print(name)


first_name = name[0:5].upper()
last_name = name[6:].upper()
last_character = name[-1]

print("first_name -> ", first_name)
print("last_name -> ", last_name)
print("last_character -> ", last_character)
