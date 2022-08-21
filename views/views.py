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


# @user_login_required
# def inner(request):
#     return render(request, 'inner-page.html')


# def login(request):
#     return render(request, 'login.html')

@user_login_required
def forgetPwd(request):
    return render(request, 'forgetPwd.html')


@user_login_required
def sroom(request):
    return render(request, 'StudyRoom.html')


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
    no = request.GET.get('no')
    name = request.GET.get('name')
    r = requests.get(
        f'{root}/get_critic_reviews/',
        params={'no': no, 'name': name},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    data = r.json()
    studyrooms = data['data']
    return render(request, 'Sroom-together.html', {'studyrooms': studyrooms})


# def register(request):
#     return render(request, 'register.html')

# def ForgetPwd(request):
#     return render(request, 'ForgetPwd.html')

# def ForgetPwd(request):
#     if request.method == 'GET':
#         return render(request, 'ForgetPwd.html')
#
#     user_id = request.POST['user_id']
#
#     r = requests.get(
#         f'{root}auth/forget/{user_id}',
#     )
#
#     result = r.json()
#     # studyrooms = result['data']
#
#     if result['success'] is True:
#         ret = redirect('/ForgetPwd/')
#         messages.success(request, '請去郵箱驗證，並重設密碼')
#         return ret
#     else:
#         messages.error(request, '查無此帳號')
#         return redirect('/ForgetPwd/')
#         return ret


# def ForgetPwdReset(request):
#     return render(request, 'ForgetPwdReset.html')


def PrivacyPolicies(request):
    return render(request, 'PrivacyPolicies.html')


# # 登入前開發人員頁面
# def beforelogin_developer(request):
#     return render(request, 'beforelogin_developer.html')

# 登入後開發人員頁面
def developer(request):
    return render(request, 'developer.html')


@user_login_required
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


@user_login_required
def Sroominpageself(request):
    return render(request, 'Sroominpage-self.html')


# 測試的自習室內部
@user_login_required
def test(request):
    return render(request, 'test.html')


def text(request):
    return render(request, 'text.html')


def award(request):
    return render(request, 'award.html')
