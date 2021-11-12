# import functools
#
# # Använd funktionen reduce (som du hittar i modulen functools) för att skapa en funktion som kontrollerar om alla värden i en lista är sanna och ger true eller false tillbaks
# # Den kan ha följande signatur all_true(l: list) -> bool
# # Exempel på körning
# #
# # all_true([True, True, True]) -> True
# #
# #
# # all_true([True, False, True, True]) -> False
#
#
# def all_true(l: list) -> bool:
#     # if False in l:
#     #     return False
#     # else:
#     #     return True
#     return functools.reduce(lambda e:    True if e else False, l)
#
# print(all_true([True, True, True]))
# print(all_true([True, True, True, False]))
#
#
