print("--------------- FUNCTION ---------------- ")


def hello(item):
    print("hello -> " + item)


items = ['1', '2', '3']

for x in items:
    hello(x)


def welcome(first_name, last_name, age):
    print("hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")


welcome("Thuta", "Sann", 22)
