# 1. Bygg en funktion som tar en tuppel med två tal som indata, och returnerar dessa i omvänd ordning. T.ex.
# t = (5, 6)
# print(swaptuple(t))
# .. ska ge följande utskrift:
# (6, 5)
#
# 2. Bygg en funktion som tar in en lista ls, och returnerar en tuppel som bygger på listan. T.ex.
# print(to_tuple([1, 2, 3]))
# ... ska ge:
# (1, 2, 3)

def swap_tuples(tup):
    return tup[::-1]

t = (5, 6)
#print(swap_tuples(t))


def to_tuple(ls):
    return tuple(ls)

print(to_tuple([1, 2, 3]))
