import requests

#
# def get_news(title, description, author):
#     url = 'http://api.example.com/books'
#     params = {'title': title, 'author': author, 'description': description}
#     r = requests.get(url, params=params)
#     news_ = r.json()
#     news_list = {'news_': news_['articles']}
#     return news_list

url = 'https://newsapi.org/v2/top-headlines?'\
      'country=us&'\
      'apiKey=46a4cd443f224d5bb7c0b7e7984f4f51'


def get_news():
    # url = 'http://api.example.com/books'
    # params = {'title': title, 'author': author, 'description': description}
    r = requests.get(url)
    news_ = r.json()
    news_list = {'news_': news_['articles']}
    return news_list
