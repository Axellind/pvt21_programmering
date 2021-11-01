# Vi skall nu sätta ihop funktionerna vi arbetat med till ett program
#
# Skapa en main-funktion i vilken ni:
# 1. Anropar funktionen för att läsa in namn och ålder
# 2. Sparar resultatet i två variabler, name och age
# 3. Anropar funkionen som skriver ut hälsningstexten med name och age som argument.
# 4. Kör main-funktionen från en if __name__ == '__main__' guard

def get_name_age():
    name = input('Namn: ')
    age = input('Ålder: ')

    return (name, age)


def print_greeting(name, age):
    print(f'{name} är {age} år gammal.')

def main():
    info = get_name_age()
    # name, age = info[0], info[1] # fult
    name, age = info  # snyggt
    print_greeting(name, age)


if __name__ == '__main__':
    main()


