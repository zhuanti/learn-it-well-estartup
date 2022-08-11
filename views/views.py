import requests
from django.contrib import messages
from django.shortcuts import render, redirect
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

# 顯示個人資料
@user_login_required
def Udetail(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}user/detail/',
        params={'user_id': user_id},
        # 'user_id': request.COOKIES['user_id'],
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    user = result['data']
    return render(request, 'UserDetail.html', {'user': user})

# 編輯個人資料(修改版)
@user_login_required
def EditUserDetail(request):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id']
        r = requests.get(
            f'{root}user/detail/',
            params={'user_id': user_id},
            # 'user_id': request.COOKIES['user_id'],
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        user = result['data']
        return render(request, 'editUserDetail.html', {'user': user})

    name = request.POST['name']
    live = request.POST['live']
    borth = request.POST['borth']

    data = {
        'user_id': request.COOKIES['user_id'],
        'name': name,
        'live': live,
        'borth': borth
    }
    # user_id = request.COOKIES['user_id']
    r = requests.post(
        f'{root}user/detail/edit/',
        # params={'user_id': user_id},
        data=data,
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()

    # if result['success'] is True:
    #     ret = redirect('/reviews/')
    #     ret.set_cookie('sessionid', result['sessionid'])
    #     # ret.set_cookie('sessionid', result['sessionid'], max_age=60 * 60) 登入時間
    #     ret.set_cookie('user_id', user_id)
    #     return ret
    # else:
    #     return redirect('/login/')

    if result['success'] is True:
        ret = redirect('/userdetail')
        messages.success(request, '已修改資料成功')
        return ret
    else:
        messages.error(request, '生日格式填寫錯誤，請重新修改')
        return redirect('/edituser-detail')


    # return render(request, 'UserDetail.html', {'message': result['message']})

# @user_login_required
# def EditUserDetail(request):
#     if request.method == 'GET':
#         user_id = request.COOKIES['user_id']
#         r = requests.get(
#             f'{root}user/detail/',
#             params={'user_id': user_id},
#             # 'user_id': request.COOKIES['user_id'],
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         user = result['data']
#         return render(request, 'editUserDetail.html', {'user': user})
#
#     id = request.POST.get['user.id']
#     name = request.POST.get['user.name']
#     live = request.POST.get['user.live']
#     borth = request.POST.get['user.borth']
#
#     data = {
#         'id': id,
#         'name': name,
#         'live': live,
#         'borth': borth
#     }
#
#     user_id = request.COOKIES['user_id']
#     r = requests.post(
#         f'{root}user/detail/edit/',
#         params={'user_id': user_id},
#         cookies={'sessionid': request.COOKIES['sessionid']},
#         data=data
#     )
#     result = r.json()
#     user = result['data']
#     return render(request, 'UserDetail.html', {'user': user})

    # user_id = request.COOKIES['user_id'],
    # r = requests.get(
    #    f'{root}user/detail/edit/',
    #    params={'user_id': user_id},
    #    # 'user_id': request.COOKIES['user_id'],
    #    cookies={'sessionid': request.COOKIES['sessionid']}
    # )
    # result = r.json()
    # user = result['data']
    # return render(request, 'editUserDetail.html', {'user': user})


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


# 問題列表
@user_login_required
def qus(request):
    r = requests.get(
        f'{root}discusroom/qus/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    discussroom_questions = result['data']
    return render(request, 'inpage.html', {'discussroom_questions': discussroom_questions})


# 新增房間-科目
# @user_login_required
# def addroom_subject(request):
#     r = requests.get(
#         f'{root}discusroom/addroom_subject/',
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     subjects = result['data']
#     return render(request, 'DiscusRoom.html', {'subjects': subjects})

# 新增房間
@user_login_required
def addroom(request):
    if request.method == 'GET':
        return render(request, 'DiscusRoom.html')

    no = request.POST['ano']
    subject_no_id = request.POST['asubject_no']
    name = request.POST['aname']
    total_people = request.POST['atotal_people']

    data = {
        'no': no,
        'subject_no_id': subject_no_id,
        'name': name,
        'total_people': total_people,
    }

    r = requests.post(
        f'{root}/discusroom/addroom/',
        data=data,
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    subjects = result['data']
    # return render(request, 'DiscusRoom.html', {'subjects': subjects})

    if result['success'] is True:
        ret = redirect('/discusroom')
        messages.success(request, '已新增房間成功')
        return ret
    else:
        messages.error(request, '新增房間失敗')
        return redirect('/discusroom')
        return ret


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

# def ForgetPwd(request):
#     return render(request, 'ForgetPwd.html')

def ForgetPwd(request):
    if request.method == 'GET':
        return render(request, 'ForgetPwd.html')

    user_id = request.POST['user_id']

    r = requests.get(
        f'{root}auth/forget/{user_id}',
    )

    result = r.json()
    # studyrooms = result['data']

    if result['success'] is True:
        ret = redirect('/ForgetPwd/')
        messages.success(request, '請去郵箱驗證，並重設密碼')
        return ret
    else:
        messages.error(request, '查無此帳號')
        return redirect('/ForgetPwd/')
        return ret


def ForgetPwdReset(request):
    return render(request, 'ForgetPwdReset.html')


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
# 測試的自習室內部
def test(request):
    return render(request, 'test.html')


# 測試用討論室內部
def WebChatTest(request):
    return render(request, 'web_chat_test.html')


def text(request):
    return render(request, 'text.html')
