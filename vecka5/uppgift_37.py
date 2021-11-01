def get_name_age():
    age = input('Ålder: ')
    name = input('Namn: ')

    return (age, name)


def print_greeting(info):
    print(f'{info[1]} är {info[0]} år gammal.')


info = get_name_age()
print_greeting(info)