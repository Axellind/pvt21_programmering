# 1. Skapa en funktion som ger oss en slumpmässig punkt i tre dimensioner. Det vill säga (x, y, z)
#
# 2. Skapa en funktion som skriver ut en sådan punkt på ett snyggt sätt
# 3. Skapa en funktion kallad translate som tar en punkt (x, y, z) och en annan tuple med tre värden,
# vi kan kalla dom (d_x, d_y, d_z) och ger som resultat(returvärde) en ny punkt (x+d_x, y+d_y, z+d_z)
#
#
# Tänk efter först hur du kan testa att dina funktioner fungerar
# Försök lösa problemet med hjälp av tuple unpacking snarare än genom att använda index.
import random


def get_random_coordinates(x_min=-10, x_max=10, y_min=-10, y_max=10, z_min=-10, z_max=10):
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    z = random.randint(z_min, z_max)

    return x, y, z


def print_coordinates(x, y, z):
    print(f'X: {x}\nY: {y}\nZ: {z}')


def translate(first_coord, second_coord):
    x, y, z = first_coord
    d_x, d_y, d_z = second_coord
    return x + d_x, y + d_y, z + d_z

test1 = get_random_coordinates()
test2 = get_random_coordinates()

print_coordinates(*test1)
print('-'*50)

print_coordinates(*test2)
print('-'*50)

print_coordinates(*translate(test1, test2))
