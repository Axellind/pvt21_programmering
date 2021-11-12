# Vi har gått igenom "".format(..) och % (...) syntaxen. Här är en övning på detta!
# 1. Leta upp en tidigare lösning på en uppgift som innehåller f-strings. Gör en kopia på filen, och byt alla f-strings mot .format. Jämför filerna. Vilken syntax föredrar ni?
# 2. Gör om samma övning fast byt till % (...) syntaxen.
# 3. Går det att göra motsvarande {xyz:20} m.h.a format() eller % syntaxen? D.v.s att kräva ett visst antal tecken utrymme vid utskrift. Googla och läs på, experimentera!
# 4. Samma som (3), fast för vänster, höger, mittenjustering (d.v.s det vi gör med <, > och ^ i f-strings).
# Tips: % tuple syntaxen är mycket lik printf i C/C++, så om du kan det så känner du igen dig. T.ex. betyder %s sträng, och %d tal.


import requests
from pprint import pprint

url = 'https://proagile.se/api/publicEvents'

results = requests.get(url).json()
#pprint(results)

def find_courses(year, month):
    for course in results:
        if course["startDate"][:4] == year and course.get('endDate', course['startDate'])[:4] == year:
            if course["startDate"][5:7] == month and course.get('endDate', course["startDate"])[5:7] == month:
                print(f'Kursnamn: {course["courseName"]}, {course["formattedDurationSv"]}, {course.get("location", "Location finns ej!")}')
                print(f'Startdatum: {course["startDate"]:15}')
                print(f'Slutdatum: {course.get("endDate", course["startDate"]):15}')
                print()


find_courses('2021', '11')


