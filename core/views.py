from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def city(request):
    return render(request, 'city.html')