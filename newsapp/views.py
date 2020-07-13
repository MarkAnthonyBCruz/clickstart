from django.shortcuts import render
from newsapi import NewsApiClient
import requests
import dateutil.parser
import datetime
import json
# Create your views here.

def news(request):
    newsapi = NewsApiClient(api_key='4f1571a2b1af4f2089d6ab2d33d67109')
    topheadlines = newsapi.get_top_headlines(sources="engadget")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []
    auth = []
    orl = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(dateutil.parser.parse(myarticles['publishedAt']))
        auth.append(myarticles['author'])
        orl.append(myarticles['url'])

    mylist = zip(news, desc, img, date, auth, orl)


    return render(request, 'newsapp/news.html', context = {"mylist": mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key='4f1571a2b1af4f2089d6ab2d33d67109')
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []
    auth = []
    orl = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(dateutil.parser.parse(myarticles['publishedAt']))
        auth.append(myarticles['author'])
        orl.append(myarticles['url'])

    mylist = zip(news, desc, img, date, auth, orl)


    return render(request, 'newsapp/news.html', context = {"mylist": mylist})

def tws(request):
    newsapi = NewsApiClient(api_key='4f1571a2b1af4f2089d6ab2d33d67109')
    topheadlines = newsapi.get_top_headlines(sources="the-wall-street-journal")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []
    auth = []
    orl = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(dateutil.parser.parse(myarticles['publishedAt']))
        auth.append(myarticles['author'])
        orl.append(myarticles['url'])

    mylist = zip(news, desc, img, date, auth, orl)



    return render(request, 'newsapp/news.html', context = {"mylist": mylist})


def corona(request):
    """url = 'https://covid-193.p.rapidapi.com/statistics'

    querystring = {"country": "Philippines"}

    headers = {
        'x-rapidapi-host': 'covid-193.p.rapidapi.com',
        'x-rapidapi-key': 'be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041'
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()


    data = response['response']
    d = data[0]
    print(d)

    context = {

        'all': d['cases']['total'],
        'recovered': d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'critical': d['cases']['critical'],
        'time': dateutil.parser.parse(d['time'])

    }"""

    return render(request, 'newsapp/corona.html')
