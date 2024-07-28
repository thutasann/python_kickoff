print("--------------- DICTIONARY ---------------- ")

# dictionary = A changable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allows us to access a value quickly

capitals = {
    "USA": "Washiton DC",
    "India": "New Dehli",
    "China": "Beijing",
    "Russia": "Moscow"
}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Los Angeles"})
capitals.pop("China")

print("Russia ->", capitals["Russia"])
print(capitals.get('China'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print('key -> ', key)
    print('value -> ', value)
