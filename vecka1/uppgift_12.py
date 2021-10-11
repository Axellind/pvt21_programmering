def is_it_too_long(namn, maxlangd):
    return int(len(namn)) > maxlangd

def main():
    students = []
    while True:
        namn = input("Vad heter du?")
        students.append(namn.capitalize())
        if namn == "Klart":
            break

    try:
        maxlangd = int(input("What is the maximum length of the name?"))
    except ValueError:
        maxlangd = 5

    for name in students:
        if is_it_too_long(name, maxlangd):
            print(f"{name} är för långt!")


if __name__ == '__main__':
    main()