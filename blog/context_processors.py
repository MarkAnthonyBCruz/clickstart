import requests
import string
import dateutil.parser
from django.utils import timezone
from .models import Post


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1b453b589a0691c857ddc95f0921df69'
    city = 'Manila'

    r = requests.get(url.format(city)).json()

    return {
        'date': timezone.now(),
        'city': city,
        'temperature': r['main']['temp'],
        "description": r['weather'][0]['description'].capitalize(),
        'icon': r['weather'][0]['icon'],
    }

def crona(request):
    url = 'https://covid-193.p.rapidapi.com/statistics'

    querystring = {"country": "Philippines"}

    headers = {
        'x-rapidapi-host': 'covid-193.p.rapidapi.com',
        'x-rapidapi-key': 'be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041'
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']
    d = data[0]

    return {

        'all': d['cases']['total'],
        'recovered': d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'critical': d['cases']['critical'],
        'time': dateutil.parser.parse(d['time'])

    }

def quotes(request):

    url = 'https://api.quotable.io/random'

    quote = requests.get(url).json()

    return {
            'quote': quote['content'],
            'author': quote['author'],
            'tags': quote['tags']
    }

  





