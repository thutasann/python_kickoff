# list = used to store multiple items in a single variable

foods = ["pizza", "hamburger", "hotdog", "spaghetti"]

foods[0] = 'sushi'

foods.append("ice-cream")
foods.remove("hotdog")
foods.insert(0, "cake")
foods.sort()

print(foods[0])

for food in foods:
    print("food -> " + food)
