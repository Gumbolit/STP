import requests
from django.shortcuts import render
from .models import City
from .forms import CitiForm

# Create your views here.
def index(request):
    appid='01a00bf0b278ae63c7b0ba81f8599faf'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        submit_button = request.POST.get('send')
        if(submit_button == 'append'):
            form = CitiForm(request.POST)
            form.save()
        if(submit_button == 'delet'):
            try:
                City.objects.get(name=request.POST['name']).delete()
            except City.MultipleObjectsReturned:
                city = City.objects.filter(name=request.POST['name']).order_by('id').last().delete()
                print(city)

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