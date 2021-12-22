import datetime
import requests
from bs4 import BeautifulSoup
from webapp.models import Movies, Upcoming
from webapp import db


def top100_scraper():
    headers = {"Accept-Language": "en-US, en;q=0.5"}

    url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")

    titles = []
    genres = []
    years = []
    lengths = []
    imdb_rates = []
    meta_scores = []
    descriptions = []
    directors = []
    photos = []

    movie_div = soup.find_all('div', class_="lister-item mode-advanced")
    for container in movie_div:
        title = container.h3.a.text
        titles.append(title)

        genre = container.find('span', class_='genre').text.strip('\n').strip()
        genres.append(genre)

        year = container.h3.find('span', class_="lister-item-year text-muted unbold").text.strip('()')
        years.append(year)

        length_in_min = container.p.find('span', class_="runtime").text.split()[0] if container.p.find('span',
                                                                                                       class_="runtime") else '-'
        lengths.append(length_in_min)

        imdb_rate = float(container.strong.text)
        imdb_rates.append(imdb_rate)

        meta_score = container.find('span', class_="metascore").text.strip() if container.find('span',
                                                                                               class_="metascore") else '-'
        meta_scores.append(meta_score)

        description = container.find('div', class_="ratings-bar").find_next_sibling("p").text.strip()
        descriptions.append(description)

        director = container.find('p', class_="").a.text
        directors.append(director)

        photo = container.find('div', class_="lister-item-image float-left").a.img['loadlate']
        photos.append(photo)

        movie = Movies.query.filter_by(title=title).first()
        if movie:
            break
        else:
            new_movie = Movies(title=title, genre=genre, year=year, length_in_min=length_in_min,
                               imdb_rate=imdb_rate,
                               meta_score=meta_score, description=description, director=director, photo_link=photo)
            db.session.add(new_movie)
            db.session.commit()


today = str(datetime.date.today())
today.split('-')
year, month, day = today.split('-')


def upcoming_movies_scraper():
    headers = {"Accept-Language": "en-US, en;q=0.5"}

    url = f"https://www.imdb.com/movies-coming-soon/{year}-{month}/?ref_=cs_dt_nx"

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")

    # Data type lists.
    titles = []
    genres = []
    lengths = []
    descriptions = []
    directors = []
    photos = []

    movie_div = soup.find_all('div', class_="list_item odd")
    for container in movie_div:
        # Name
        name = container.h4.a.text
        titles.append(name)

        # Genre
        genre = container.p.span.text.split(" ")
        lst = []
        if type(genre) == type(lst):
            genre = genre[0]
        genres.append(genre)

        length_in_min = container.find('p', class_="cert-runtime-genre").time.text.split()[0] if container.find('p',
                                                                                                                class_="cert-runtime-genre").time else '-'
        lengths.append(length_in_min)

        description = container.find('div', class_="outline").text.strip() if container.find('div',
                                                                                     class_="outline").text else '-'
        descriptions.append(description)

        director = container.find('div', class_="txt-block").span.a.text
        directors.append(director)

        photo = container.find('div', class_="hover-over-image zero-z-index").img['src']
        photos.append(photo)

        movie = Upcoming.query.filter_by(title=name).first()
        if movie:
            break
        else:
            new_movie = Upcoming(title=name, genre=genre, length_in_min=length_in_min, description=description, director=director,
                                 photo_link=photo)
            db.session.add(new_movie)
            db.session.commit()

    movie_div = soup.find_all('div', class_="list_item even")
    for container in movie_div:
        # Name
        name = container.h4.a.text
        titles.append(name)

        # Genre
        genre = container.p.span.text
        lst = []
        if type(genre) == type(lst):
            genre = genre[0]
        genres.append(genre[0])

        length_in_min = container.find('p', class_="cert-runtime-genre").time.text.split()[0] if container.find('p',
                                                                                                                class_="cert-runtime-genre").time else '-'
        lengths.append(length_in_min)

        description = container.find('div', class_="outline").text.strip() if container.find('div',
                                                                                     class_="outline").text else '-'
        descriptions.append(description)

        director = container.find('div', class_="txt-block").span.a.text
        directors.append(director)

        photo = container.find('div', class_="hover-over-image zero-z-index").img['src']
        photos.append(photo)

        movie = Upcoming.query.filter_by(title=name).first()
        if movie:
            break
        else:
            new_movie = Upcoming(title=name, genre=genre, length_in_min=length_in_min, description=description, director=director,
                                 photo_link=photo)
            db.session.add(new_movie)
            db.session.commit()


def init_scraper():
    upcoming_movies_scraper()
    top100_scraper()
