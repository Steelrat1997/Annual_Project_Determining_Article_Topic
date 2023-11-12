import requests
from bs4 import BeautifulSoup

ARTICLE_URL_TEMPLATE = 'https://habr.com/ru/articles/{}/'



def get_article(article_id):
    # выгрузка документа
    r = requests.get(ARTICLE_URL_TEMPLATE.format(article_id))

    if r.status_code != 200:
        print('Status code is not ok:', r.status_code)

    # парсинг документа
    soup = BeautifulSoup(r.text, 'html5lib') # instead of html.parser
    
    doc = {}
    doc['id'] = article_id
    if not soup.find("h1", {"class": "tm-title"}):
        # такое бывает, если статья не существовала или удалена
        return None
    else:
        doc['title'] = soup.find("h1", {"class": "tm-title"}).text
        doc['text'] = soup.find("div", {"id": "post-content-body"}).get_text(separator=' ')
        doc['time'] = soup.find("time")["title"]
        doc['hubs'] = "|".join(list(map(lambda s: s.text, soup.find_all('span', {'class': 'tm-publication-hub__link-container'}))))
        doc['tags'] = "|".join(list(map(lambda s: s.text, soup.find_all('a', {'class': 'tm-tags-list__link'}))))

    return doc