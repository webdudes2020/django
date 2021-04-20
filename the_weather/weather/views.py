from django.shortcuts import render


def index(requests):
    return render(request, 'weather/weather.html')
