import requests
from pprint import pprint

URL = 'https://www.omdbapi.com/'
search_results = {}

with open('api_key') as f:
    API_KEY = f.readline()


def get_movie_info(name):
    parameters = {'t': name, 'apiKey': API_KEY}
    r = requests.get(URL, params=parameters).json()
    print_movie_info(r)


def search_movie(movie):
    parameters = {'s': movie, 'apiKey': API_KEY}

    r = requests.get(URL, params=parameters).json()
    if r["Response"] == 'True':
        print('response true: ')
        for number, movie in enumerate(r["Search"]):
            search_results[number+1] = movie


def display_search_results():
    for number, info in search_results.items():
        print(f'{number}. {info["Title"]}')

    while True:
        selected_movie = input('Vilken film vill du veta mer om?')
        if selected_movie == 'q':
            break
        r = search_results.get(int(selected_movie))
        print_movie_info(r)
        print()


def print_movie_info(r):
    print(f'Resultat från IMDB:\n{r["Title"]} ({r["Year"]}) regisserades av {r.get("Director", "")}.')
    print(f'Skådisar: {r.get("Actors", "")}\nIMDB betyg: {r.get("imdbRating", "")}\nAwards: {r.get("Awards", "")}\nLängd: {r.get("Runtime", "")}')


def main():
    user_search = input("Sök efter film: ").strip()

    # get_movie_info(user_search)
    search_movie(user_search)
    display_search_results()


main()
