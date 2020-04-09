from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import City
from .forms import CityForm
import requests


def index(request):
    url = r"https://api.openweathermap.org/data/2.5/weather?q={}&appid=ca6b648092fb0cc05785327267297020&units=metric"
    err_msg = ''
    success_msg = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('name')
            resp = requests.get(url.format(city))
            if resp.status_code == 200:
                city_count = City.objects.filter(name=city).count()
                if city_count == 0:
                    form.save()
                    success_msg = 'City added successfully!'
                else:
                    err_msg = "City already exists!"
            else:
                err_msg = "Invalid city!"
        else:
            err_msg = "Invalid form submission!"

    cities = City.objects.all()

    form = CityForm()
    weather_data = list()

    for city in cities:
        resp = requests.get(url.format(city)).json()

        description = resp['weather'][0]['description']
        icon = resp['weather'][0]['icon']
        temperature = resp['main']['temp']
        country = resp['sys']['country']

        city_weather = {
            'city': city.name,
            'description': description,
            'icon': icon,
            'temperature': temperature,
            'country': country
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data,
               'form': form,
               'err_msg': err_msg,
               'success_msg': success_msg}

    return render(request, 'weatherapp/index.htm', context=context)


def delete_city(request, city):
    City.objects.filter(name=city).delete()
    return redirect('home')
