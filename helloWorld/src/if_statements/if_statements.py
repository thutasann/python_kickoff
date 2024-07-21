print("---------------- IF STATEMENT ---------------- ")

age = int(input("how old are you ? :"))

if age == 100:
    print("you are a century old!")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("you haven't born yet!")
else:
    print("You are a child")
