import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    appid='01a00bf0b278ae63c7b0ba81f8599faf'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city="London"
    res = requests.get(url.format(city)).json()


    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]['icon']

    }
    context = {'info': city_info}

    return render(request, 'weather/index.html', context)