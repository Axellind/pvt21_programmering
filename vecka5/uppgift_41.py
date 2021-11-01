# Ett alternativ till att låta funktionen från föregående övningar returnera en tuple med namn och ålder är
# att kapsla in den informationen i en klass.
#
# Ni kan utgå från den cheat-sheet som finns länkad under material.
#
# 1. Skap en klass Person som har ett namn och en ålder
# 2. Skriv om funktionen som läser in namn och ålder så att den nu returnerar en instans av klassen Person

class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        print("__init__", name, age)
        self.name = name
        self.age = age


def read_person() -> Person:
    name = input("Name: ")
    age = int(input("Age: "))
    return Person(name, age)


def greeting(name, age):
    return f"{name} är {age} år gammal"


def greet_person(person: Person) -> str:
    return print(f"{person.name} är {person.age} år gammal")
    pass
    # Skall ta emot ett argument person, som är en instans av klassen Person
    # Ger som returvärde en textsträng ex: "Kevin är 26 år gammal"


def main():
    p = read_person()
    greet_person(p)
    # print(p.name)
    # print(p.age)


if __name__ == '__main__':
    main()

