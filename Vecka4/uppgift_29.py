import requests
from pprint import pprint

url = 'https://proagile.se/api/publicEvents'

results = requests.get(url).json()

#pprint(results)

for course in results:
    print(f' {course["courseName"]}, startar den {course["startDate"]}')
