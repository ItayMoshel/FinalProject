# import datetime
# import requests
# from bs4 import BeautifulSoup
#
# today = str(datetime.date.today())
# today.split('-')
# year, month, day = today.split('-')
#
#
# def upcoming_movies_scraper():
#     headers = {"Accept-Language": "en-US, en;q=0.5"}
#
#     url = f"https://www.imdb.com/movies-coming-soon/{year}-{month}/?ref_=cs_dt_nx"
#
#     results = requests.get(url, headers=headers)
#     soup = BeautifulSoup(results.text, "html.parser")
#
#     # Data type lists.
#     titles = []
#     genres = []
#     lengths = []
#     descriptions = []
#     directors = []
#     photos = []
#
#     movie_div = soup.find_all('div', class_="list_item odd")
#     for container in movie_div:
#         # Name
#         name = container.h4.a.text
#         titles.append(name)
#
#         # Genre
#         genre = container.p.span.text.split(" ")
#         lst = []
#         if type(genre) == type(lst):
#             genre = genre[0]
#         genres.append(genre)
#
#         length_in_min = container.find('p', class_="cert-runtime-genre").time.text.split()[0] if container.find('p',
#                                                                                                                 class_="cert-runtime-genre").time else '-'
#         lengths.append(length_in_min)
#
#         description = container.find('div', class_="outline").text
#         descriptions.append(description)
#
#         director = container.find('div', class_="txt-block").span.a.text
#         directors.append(director)
#
#         photo = container.find('div', class_="hover-over-image zero-z-index").img['src']
#         photos.append(photo)
#
#     movie_div = soup.find_all('div', class_="list_item even")
#     for container in movie_div:
#         # Name
#         name = container.h4.a.text
#         titles.append(name)
#
#         # Genre
#         genre = container.p.span.text
#         lst = []
#         if type(genre) == type(lst):
#             genre = genre[0]
#         genres.append(genre[0])
#
#         length_in_min = container.find('p', class_="cert-runtime-genre").time.text.split()[0] if container.find('p',
#                                                                                                                 class_="cert-runtime-genre").time else '-'
#         lengths.append(length_in_min)
#
#         description = container.find('div', class_="outline").text if container.find('div', class_="outline").text else '-'
#         descriptions.append(description)
#
#         director = container.find('div', class_="txt-block").span.a.text
#         directors.append(director)
#
#         photo = container.find('div', class_="hover-over-image zero-z-index").img['src']
#         photos.append(photo)
#
#         print(description)
#
#     print(len(descriptions))
#
# upcoming_movies_scraper()
#
# print(f"""
#             action: {len(top_by_action)} {top_by_action}
#
#             drama: {len(top_by_drama)} {top_by_drama}
#
#             thriller: {len(top_by_thriller)} {top_by_thriller}
#
#             crime: {len(top_by_crime)} {top_by_crime}
#
#             comedy: {len(top_by_comedy)} {top_by_comedy}
# """)
#
#
#
