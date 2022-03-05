from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def login(request):
    return render(request, 'login.html')


def forgetPwd(request):
    return render(request, 'ForgetPwd.html')


def register(request):
    return render(request, 'register.html')


def Udetail(request):
    return render(request, 'UserDetail.html')


def sroom(request):
    return render(request, 'StudyRoom.html')


def droom(request):
    return render(request, 'DiscusRoom.html')


def achievement(request):
    return render(request, 'achievement.html')


def report(request):
    return render(request, 'report.html')


def Splan(request):
    return render(request, 'StudyPlan.html')