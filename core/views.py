from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def login(request):
    return render(request, 'login.html')


def ForgetPwd(request):
    return render(request, 'ForgetPwd.html')


def register(request):
    return render(request, 'register.html')