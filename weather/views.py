import requests
from django.shortcuts import render
from .models import City
from .forms import CitiForm
from .forms import UserEventForm
# Create your views here.


def index(request):
    appid='01a00bf0b278ae63c7b0ba81f8599faf'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CitiForm(request.POST)
        form.save()


    form=CitiForm()

    citis = City.objects.all()

    all_cities=[]

    for city in citis:
        res = requests.get(url.format(city.name)).json()
        city_info = {
         'city': city.name,
         'temp': res["main"]["temp"],
         'icon': res["weather"][0]['icon']
         }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form':form}

    return render(request, 'weather/index.html', context)


def create(request):
    form = 0
    if request.method == 'POST':
        form = UserEventForm(request.POST)
        form.save()
    context = {
        'form': form
        }

    return render(request, 'weather/create_event.html', context)

