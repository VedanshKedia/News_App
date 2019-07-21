# from django.shortcuts import render
# from . import services
# from django.views import generic
from django.shortcuts import render
# from django.http import request
import requests
# Create your views here.


url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=46a4cd443f224d5bb7c0b7e7984f4f51'

# response = requests.get(url)


def home(request):
    # def get(self, request):
    #     news_list = services.get_news()
    #     return render(request, 'home.html', news_list)
    response = requests.get(url)
    newsdata = response.json()
    articles = newsdata['articles']
    authors = []
    titles = []
    descriptions = []
    urlToImages = []
    contents = []
    articleurls = []
    for article in articles:
        authors.append(article['author'])
        titles.append(article['title'])
        descriptions.append(article['description'])
        contents.append(article['content'])
        urlToImages.append(article['urlToImage'])
        articleurls.append(article['url'])

    data = zip(authors, titles, descriptions, urlToImages, contents, articleurls)
    # return render(request, 'home.html', {'authors':authors, 'titles':titles, 'description': descriptions})
    return render(request, 'home.html', {'data': data})

    # return  render(request, 'home.html', {'newdsata'})
