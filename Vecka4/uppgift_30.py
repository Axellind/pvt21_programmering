import requests
from pprint import pprint

url = 'https://proagile.se/api/publicEvents'

results = requests.get(url).json()
#pprint(results)
#print()

def find_courses(year, month):
    for course in results:
        # if "endDate" not in course:
        #     print('FOUND A COURSE WITHOUT END DATE: ', course)
        #     continue
        #
        # else:
        if course["startDate"][:4] == year and course.get('endDate', course['startDate'])[:4] == year:
            if course["startDate"][5:7] == month and course.get('endDate', course["startDate"])[5:7] == month:
                print(f'Kursnamn: {course["courseName"]}, {course["formattedDurationSv"]}, {course.get("location", "Location finns ej!")}')
                print(f'Startdatum: {course["startDate"]}')
                print(f'Slutdatum: {course.get("endDate", course["startDate"])}')
                print()


find_courses('2021', '10')