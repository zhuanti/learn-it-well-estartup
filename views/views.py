import requests
from django.shortcuts import render
from core.settings import API_URL as root
from utils.decorators import user_login_required


# # 登入前首頁畫面
# def beforelogin_index(request):
#     return render(request, 'beforelogin_index.html')

# 登入後首頁畫面
def index(request):
    return render(request, 'index.html')


@user_login_required
def inner(request):
    return render(request, 'inner-page.html')


# def login(request):
#     return render(request, 'login.html')

@user_login_required
def forgetPwd(request):
    return render(request, 'forgetPwd.html')


@user_login_required
def Udetail(request, pk):
    r = requests.get(f'{root}/get/{pk}/')
    result = r.json()
    if result['success'] is True:
        user = result['data']
        return render(request, 'UserDetail.html', {'user': user})
    else:
        message = result['message']
        return render(request, 'result.html', {'message': message})


@user_login_required
def sroom(request):
    return render(request, 'StudyRoom.html')


@user_login_required
def droom(request):
    r = requests.get(
        f'{root}discusroom/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    discussrooms = result['data']
    return render(request, 'DiscusRoom.html', {'discussrooms': discussrooms})


@user_login_required
def achievement(request):
    return render(request, 'achievement.html')  # 完成


@user_login_required
def report(request):
    return render(request, 'report.html')  # 完成


@user_login_required
def Splan(request):
    return render(request, 'StudyPlan.html')


@user_login_required
def SroomSelf(request):
    return render(request, 'Sroom-self.html')


@user_login_required
def Sroomtogether(request):
    r = requests.get(
        f'{root}studyroom/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    studyrooms = result['data']
    return render(request, 'Sroom-together.html', {'studyrooms': studyrooms})
    # return render(request, 'Sroom-together.html')


# def register(request):
#     return render(request, 'register.html')

# def forgetPwd(request):
#     return render(request, 'forgetPwd.html')

def ForgetPwd(request):
    return render(request, 'ForgetPwd.html')


def ForgetPwdUpdate(request):
    return render(request, 'ForgetPwdUpdate.html')


def PrivacyPolicies(request):
    return render(request, 'PrivacyPolicies.html')


# # 登入前開發人員頁面
# def beforelogin_developer(request):
#     return render(request, 'beforelogin_developer.html')

# 登入後開發人員頁面
def developer(request):
    return render(request, 'developer.html')


@user_login_required
def inpage(request):
    return render(request, 'inpage.html')


@user_login_required
def Sroominpage(request):
    return render(request, 'Sroominpage.html')


@user_login_required
def Sroominpageself(request):
    return render(request, 'Sroominpage-self.html')


@user_login_required
def DayReport(request):
    return render(request, 'day-report.html')


@user_login_required
def WeekReport(request):
    return render(request, 'week-report.html')


@user_login_required
def EditUserDetail(request):
    return render(request, 'edit UserDetail.html')


@user_login_required
# 測試的自習室內部
def test(request):
    return render(request, 'test.html')


# 測試用討論室內部
def WebChatTest(request):
    return render(request, 'web_chat_test.html')
