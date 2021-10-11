# 15.1 Implementera ett program som räknar ord och bokstäver i en text
# 15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com) och skriv ut hur många vokaler som finns i strängen. Tips: "a" in "abcd" är True!
# 15.3 Göteborgsvarvet, vilken placering kom XYZ på? Implementera resten av detta program:
# runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
# vem = input(“Ange löpare du söker placering för”)


text = """
En app som kan laddas ned till vuxenleksaken ska påpeka
dem från finland som kommit nära någon som infekterats med
ett lätt botat virus. – Jag tycker att ni i de landet bredvid norge borde strunta i att göra något
liknande, säger gustav vasa, kungen för
norrlands dags tidning.
Hejsan detta är lite siffror som programmet ska kunna skilja sig åt från bokstäver: 1234 1 2 3 12345678910
"""

VOKALER = "aeiouyåäö"


def count_vokaler(t):
    i = 0
    for letter in t:
        if letter in VOKALER:
            i += 1
    return i


def countLetterAndDigits():
    numberCount = 0
    letterCount = 0

    for character in text:
        if character.isdigit():  # för varje siffra så läggs +1 till i numberCount
            numberCount += 1
        elif character.isalpha():  # för varje bokstav så läggs +1 till i letterCount
            continue
