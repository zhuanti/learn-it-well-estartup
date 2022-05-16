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
    return render(request, 'achievement.html')  # 完成


def report(request):
    return render(request, 'report.html')  # 完成


def Splan(request):
    return render(request, 'StudyPlan.html')


def SroomSelf(request):
    return render(request, 'Sroom-self.html')


def Sroomtogether(request):
    return render(request, 'Sroom-together.html')


def register(request):
    return render(request, 'register.html')


def developer(request):
    return render(request, 'developer.html')

def inpage(request):
    return render(request, 'inpage.html')

def Sroominpage(request):
    return render(request, 'Sroominpage.html')

