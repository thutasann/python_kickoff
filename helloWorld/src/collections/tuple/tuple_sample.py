# tuple = collection which is ordered and unchangable
#       used to group together related data
print("--------------- TUPLE ---------------- ")

student = ("Thuta", 22, "Sann")

print(student.count("Thuta"))
print(student.index("Sann"))


for x in student:
    print(x)

if "Thuta" in student:
    print("Thuta is here")
