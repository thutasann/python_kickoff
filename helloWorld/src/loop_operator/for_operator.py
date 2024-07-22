import time

print("---------------- FOR LOOP OPERATOR ---------------- ")

# for loop = a statement that will execute it's block of code
#           a limited amount of times
#           while loop = unlimited
#           for loop = limited

for i in range(10):
    print("i -> ", i + 1)

print("------------------------")

for y in range(50, 100 + 1, 2):
    print("y -> ", y)


print("------------------------")

for z in "Thuta Sann":
    print("z -> ", z)

print("------------------------")

for seconds in range(10, 0, -1):
    print("seconds -> ", seconds)
    time.sleep(1)

print("Happy New Year!")
