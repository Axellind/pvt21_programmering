from math import sqrt


# Uppgift 53
# Skapa enhetstester för primtalsfaktoriseringen
# Det vi vill kontrollera är att funktionen/algoritmen vi använder för att
# ta fram alla primtalsfaktorer fungerar.
# Ni kommer märka att det blir lite komplicerat att testa eftersom


def factors(num):
    #num = int(input(">"))
    # Vi börjar med att plocka ut alla faktorer 2 ur talen num
    # Exempel: 120 = 2 * 2 * 2 * 3 * 5
    # Här finns faktorn 2 med totalt 3 gånger. Loopen nedan tar bort dom en i taget och skriver ut i terminalen
    num = get_factoring(num)
    print(num)
    return num



def get_factoring(num):
    factoring_list = []
    while num % 2 == 0:
        factoring_list.append(2)
        num = num / 2
    # Eftersom vi precis tagit bort samtliga faktorer 2 är det som återstår av talen num udda
    # Because math behöver vi bara leta primfaktorer upp till kvadratroten av num  plus 1
    # Eftersom alla faktorer 2 redan är borta räcker det att kolla udda tal
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            factoring_list.append(i)
            num = num / i

    if num > 2:
        factoring_list.append(int(num))
        #print(int(num))
    return factoring_list


if __name__ == '__main__':
    factors(36)
    factors(500000)
