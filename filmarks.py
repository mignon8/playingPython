import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_films(url):
    time.sleep(1)
    with urlopen(url) as res:
        html = res.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('.p-content-cassette__title')
    ratings = soup.select('.p-content-cassette__rate .c-rating .c-rating__score')

    films = []
    for title, rating in zip(titles, ratings):
        films.append({ 'title': title.string, 'rating': rating.string })

    return films
