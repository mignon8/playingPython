import json, random
from urllib.request import urlopen
from flask import Flask, render_template
from bs4 import BeautifulSoup
import filmarks

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    with urlopen('https://b.hatena.ne.jp/hotentry/it') as res:
        html = res.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.select('.entrylist-contents-title a')
    article = random.choice(articles)

    return json.dumps({
        'content': article.string,
        'link': article['href']
    })


@app.route("/film")
def film():
    return render_template("film.html")

@app.route("/api/film_2021")
def api_film_2021():
    # 2021年のページ数は最大101。固定じゃない場合は、urlもスクレイピングする必要がある。
    # ここでは少ない数を指定しておく。
    max_page = 5
    films_all = []
    for i in range(max_page):
        if i == 0:
            data = filmarks.get_films('https://filmarks.com/list/year/2020s/2021')
            films_all = films_all + data
        else:
            data = filmarks.get_films(f'https://filmarks.com/list/year/2020s/2021?page={i + 1}')
            films_all = films_all + data

    films_all_sorted = sorted(films_all, key=lambda x:x['rating'], reverse=True)
    return json.dumps(films_all_sorted)


if __name__ == "__main__":
    app.run(debug=True, port=5004)
