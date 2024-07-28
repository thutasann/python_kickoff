print("--------------- SET ---------------- ")

# set = collection which iis unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkins")
utensils.update(dishes)

print("differeence -> ", utensils.difference(dishes))
print("intersection ->", utensils.intersection(dishes))

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)
