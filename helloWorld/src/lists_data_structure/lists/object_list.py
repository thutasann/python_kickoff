class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


people = [
    Person("Alice", 30),
    Person("Bob", 24),
    Person("Charlie", 29)
]

for person in people:
    print(person)
