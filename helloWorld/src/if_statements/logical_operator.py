print("---------------- LOGICAL OPERATORS ---------------- ")

"""
local operators (and,or,not) = used to check if two or more conditional statements
"""
temp = int(input("What is the temperature outside?: "))

if not (temp >= 0 and temp <= 20):
    print("the temperature is bad today!")
    print("stay inside!")
elif not (temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("go outside")
