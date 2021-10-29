# Träna slicing av strängar och listor!
# Reg.nr på bilar i Sverge skrivs traditionellt* med tre bokstäver och tre siffror.
# 1. Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
# var för sig; använd slicing-syntax för att dela upp inputsträngen.
# Ange regnr: ABC663
# Bokstävsgrupp: ABC
# Siffergrupp: 663
# Låt funktionen du skapar för att dela upp registreringsnumret returnera en tuple där det första elementet är bokstavsdelen och det andra är sifferdelen.
# Ex:
# ("ABC", 663)

# 2. Bygg ett program där användaren matar in ett gäng heltal med komma emellan, och skriver ut följande:
# Ange tal med komma emellan: 1,2,3,5,100
# Första talet: 1
# Sista talet: 100
# Summan av talen: 111
# Talen baklänges: 100, 5, 3, 2, 1
# Tips: Använd slicing och inbyggda funktionen sum().
# Tips 2: Det går att lösa "Talen baklänges" på två sätt: det lätta sättet
# är med inbyggda funktionen reverse(). Det svåra sättet är med slicing syntax!
# Pröva båda :)
#
# * Vi ignorerar ny nummerskyltar med bokstav i sifferdelen

def reg_nr(nr):
    return nr[:3], nr[3:]

test = 'ABC123'

test2 = reg_nr(test)
#print(test2)


def uppgift_2(user_input):
    test = user_input.split(',')

    nummer_list = []
    for nummer in test:
        nummer_list.append(int(nummer))
    print(test)
    print(test[0])
    print(test[-1])
    print(sum(nummer_list))
    #print(sum(int(number) for number in test))
    #print(sum(map(int, test)))
    # test.reverse()
    # print(test)

    print(test[::-1])

exempel = '1,2,3,5,100'
uppgift_2(exempel)
