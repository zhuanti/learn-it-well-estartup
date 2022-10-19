import requests
from django.conf import settings

from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
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

@user_login_required
def droom(request):
    if request.method == 'POST':
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
            f'{root}discusroom/addroom/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        # subjects = result['data']
        # return render(request, 'DiscusRoom.html', {'subjects': subjects})

        if result['success'] is True:
            ret = redirect('/discusroom')
            messages.success(request, '已新增房間成功')
            return ret
        else:
            messages.error(request, '新增房間失敗')
            return redirect('/discusroom')
            return ret

    if request.method == 'GET':
        r = requests.get(
            f'{root}discusroom/all/',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        discussrooms = result['data']
        return render(request, 'DiscusRoom.html', {'discussrooms': discussrooms})

    # ret = redirect('/discusroom/#letmeopen')
    # messages.success(request, '已新增房間成功')
    # return ret


# 新增房間
# @user_login_required
# def addroom(request):
#     # if request.method == 'GET':
#     #     return render(request, 'DiscusRoom.html')
#
#     # el
#     # if request.method == 'POST':
#     no = request.POST.get['ano']
#     subject_no_id = request.POST.get['asubject_no']
#     name = request.POST.get['aname']
#     total_people = request.POST.get['atotal_people']
#         # city = request.POST.get('city')
#         # print('執行資料儲存操作...')
#         # return render(request, 'popup.html', {'city': city})
#
#     # no = request.POST['ano']
#     # subject_no_id = request.POST['asubject_no']
#     # name = request.POST['aname']
#     # total_people = request.POST['atotal_people']
#
#     data = {
#         'no': no,
#         'subject_no_id': subject_no_id,
#         'name': name,
#         'total_people': total_people,
#     }
#
#     r = requests.post(
#         f'{root}/discusroom/addroom/',
#         data=data,
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     # subjects = result['data']
#     # return render(request, 'DiscusRoom.html', {'subjects': subjects})
#
#     if result['success'] is True:
#         ret = redirect('/discusroom')
#         messages.success(request, '已新增房間成功')
#         return ret
#     else:
#         messages.error(request, '新增房間失敗')
#         return redirect('/discusroom')
#         return ret


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


# 自習室列表
@user_login_required
def Sroomtogether(request):
    r = requests.get(
        f'{root}studyroom/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    studyrooms = result['data']
    return render(request, 'Sroom-together.html', {'studyrooms': studyrooms})


# 自習室查詢
@user_login_required
def Sserch(request):
    name = request.GET.get('name')
    r = requests.get(
        f'{root}studyroom/Sserch/',
        params={'name': name},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    data = r.json()
    studyrooms = data['data']
    return render(request, 'Sroom-together.html', {'studyrooms': studyrooms})


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
        # email_template = render_to_string(
        #     'templates/ResetPasswordEmail.html',
        #     {'name': request.user.name}
        # )
        # email = EmailMessage(
        #     '做伙來讀冊-更新密碼網址',  # 電子郵件標題
        #     email_template,  # 電子郵件內容
        #     settings.EMAIL_HOST_USER,  # 寄件者
        #     ['jenny980132@gmail.com']  # 收件者
        # )
        # email.fail_silently = False
        # email.send()
        # subject = 'Thank you for registering to our site'
        # message = ' it  means a world to us '
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['jenny980132@gmail.com', ]
        # send_mail(subject, message, email_from, recipient_list)
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


# @user_login_required
# def inpage(request):
#     return render(request, 'inpage.html')


@user_login_required
# def Sroominpage(request):
#     return render(request, 'Sroominpage.html')

def Sroominpage(request, pk):
    r = requests.get(
        f'{root}studyroom/get/{pk}',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    if result['success'] is True:
        studyroom = result['data']
        return render(request, 'Sroominpage.html', {'studyroom': studyroom})
    else:
        messages.error(request, '查無此房間')
        return redirect('/studyroom-together/')
        return ret
        #
        # message = result['message']
        # return render(request, 'Sroom-together.html', {'message': message})

    # return render(request, 'Sroominpage.html')


# @user_login_required
# def Sroominpageself(request):
#     return render(request, 'Sroominpage-self.html')


# 個人自習室填寫科目資料
@user_login_required
def Sroom_self(request):
    r = requests.get(
        f'{root}studyroom/self',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    inform = result['data']
    return render(request, 'Sroom-self.html', {'inform': inform})


# 按照學姊寫的寫法https://hsinyi-lin.gitbook.io/django-rest-api-orm/api-call/%E5%91%BC%E5%8F%AB%20-%20%E6%96%B0%E5%A2%9E%E8%A9%95%E8%AB%96
    # if request.method == 'GET':
    #     return render(request, 'Sroom-self.html')
    #
    #     # no = request.POST['no']
    #     classroom_type_no_id = request.POST[2]
    #     subject_no_id = request.POST['subject_no_id']
    #     set_time_id = request.POST['set_time_id']
    #     subject_detail = request.POST['subject_detail']
    #     data = {
    #         # 'no': no,
    #         'user_id': request.COOKIES['user_id'],
    #         'classroom_type_no_id': classroom_type_no_id,
    #         'subject_no_id': subject_no_id,
    #         'set_time_id': set_time_id,
    #         'subject_detail': subject_detail,
    #     }
    # r = requests.post(
    #     f'{root}/addsub/',
    #     data=data,
    # )
    # result = r.json()
    # return render(request, 'Sroominpage-self.html', {'message': result['message']})

# 按照其他類似功能寫的寫法
#     user_id = request.COOKIES['user_id'],
#     r = requests.get(
#         f'{root}/addsub/',
#         params={'user_id': user_id},
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     if request.method == 'POST':
#         # no = request.POST['no']
#         classroom_type_no_id = request.POST[2]
#         subject_no_id = request.POST['subject_no_id']
#         set_time_id = request.POST['set_time_id']
#         subject_detail = request.POST['subject_detail']
#
#         data = {
#             # 'no': no,
#             'user_id': request.COOKIES['user_id'],
#             'classroom_type_no_id': classroom_type_no_id,
#             'subject_no_id': subject_no_id,
#             'set_time_id': set_time_id,
#             'subject_detail': subject_detail,
#         }
#
#         r = request.post(
#             f'{root}/addsub/',
#             data=data,
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         if result['success'] is True:
#             ret = redirect('/Sroominpage-self')
#             messages.success(request, '新增成功')
#             return ret
#         else:
#             messages.error(request, '新增失敗')
#             return redirect('/studyroom-self')
#             return ret
#
#     if request.method == 'GET':
#         r = requests.get(
#             f'{root}/inside/',
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         informations = result['data']
#         return render(request, 'Sroominpage-self.html', {'informations': informations})


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


@user_login_required
def award(request):
    return render(request, 'award.html')


def Sroomtogethersub(request):
    return render(request, 'Sroom-togethersub.html')

def Splan_edit(request):
    return render(request, 'Splan_edit.html')