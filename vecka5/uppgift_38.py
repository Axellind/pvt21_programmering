# Lek med tuppler! (Tuples)
# 1. Bygg en funktion som tar en tuppel med två tal som indata, och returnerar dessa i omvänd ordning. T.ex.
# t = (5, 6)
# print(swaptuple(t))
# .. ska ge följande utskrift:
# (6, 5)
# 2. Bygg en funktion som tar in en lista ls, och returnerar en tuppel som bygger på listan. T.ex.
# print(to_tuple([1, 2, 3]))
# ... ska ge:
# (1, 2, 3)



def reverse_tuple(input_tuple):
    # Går också att "return tuple(reversed(input_tuple))
    return input_tuple[::-1]

test_list = [1, 3, 5, 7, 9]
test = (1, 3, 5, 7, 9)
# print(reverse_tuple(test))
# print(reverse_tuple(test_list))

def to_tuple(input_list: list):
    return tuple(input_list)

print(to_tuple(test_list))

