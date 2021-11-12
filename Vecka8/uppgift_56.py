# Vi utgår från uppgift 16
# Använd filter-funktionen för att ta fram de rader som innehåller BEAR eller X-RAY.
# För att få det att fungera behöver du skapa en ny funktion som ger True som resultat om en textrad innehåller något av orden vi letar efter


def filter_lines():
    for words in lines:
        if "BEAR" in words or "X-RAY" in words:
            return True

def filter_2(s: str) -> bool:
    if "BEAR" in s or "X-RAY" in s:
        return True
    #return "BEAR" in s or "X-RAY" in s
        #return True

# read the file into a list of lines
with open('logfil.txt') as f:
    with open('logfil_test.txt', 'w') as f_out:
        lines = f.read().split("\n")
        f_out.writelines(filter(filter_2, f))
#       print(list(filter(filter_2, f)))

# get number of lines of the text
length = len(lines)
print(f"Number of total lines is {length}")

#for l in lines:
#    if "BEAR" in l or "X-RAY" in l:
#        print(l)



# create variables for the words you would like to search for
word1 = 'BEAR'
word2 = 'X-RAY'

#ny_list = list(filter(filter_2(lines), lines))#
#print('new list: ', ny_list)

#print(list(filter(lambda a: a if "BEAR" in a or "X-RAY" in a for words in lines), lines))

#method_name()





