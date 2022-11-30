import requests
from django.conf import settings

from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from core.settings import API_URL as root
from utils.decorators import user_login_required


# 首頁畫面
def index(request):
    if 'user_id' in request.COOKIES:
        user_id = request.COOKIES['user_id'],
        r = requests.get(
            f'{root}news/',
            params={'user_id': user_id},
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            plans = result['data']
            return render(request, 'index.html', {'plans': plans})
        else:
            return render(request, 'index.html')

    return render(request, 'index.html')


@user_login_required
def inner(request):
    return render(request, 'inner-page.html')

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
    r = requests.post(
        f'{root}user/detail/edit/',
        # params={'user_id': user_id},
        data=data,
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()

    if result['success'] is True:
        ret = redirect('/userdetail')
        messages.success(request, '已修改資料成功')
        return ret
    else:
        messages.error(request, '生日格式填寫錯誤，請重新修改')
        return redirect('/edituser-detail')

    # return render(request, 'UserDetail.html', {'message': result['message']})

# 自習室個人或多人選擇
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

# @user_login_required
# def droom(request):
#     if request.method == 'POST':
#         no = request.POST['ano']
#         subject_no_id = request.POST['asubject_no']
#         name = request.POST['aname']
#         total_people = request.POST['atotal_people']
#
#         data = {
#             'no': no,
#             'subject_no_id': subject_no_id,
#             'name': name,
#             'total_people': total_people,
#         }
#
#         r = requests.post(
#             f'{root}discusroom/addroom/',
#             data=data,
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         # subjects = result['data']
#         # return render(request, 'DiscusRoom.html', {'subjects': subjects})
#
#         if result['success'] is True:
#             ret = redirect('/discusroom')
#             messages.success(request, '已新增房間成功')
#             return ret
#         else:
#             messages.error(request, '新增房間失敗')
#             return redirect('/discusroom')
#             return ret
#
#     if request.method == 'GET':
#         r = requests.get(
#             f'{root}discusroom/all/',
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         discussrooms = result['data']
#         return render(request, 'DiscusRoom.html', {'discussrooms': discussrooms})
#
#     # ret = redirect('/discusroom/#letmeopen')
#     # messages.success(request, '已新增房間成功')
#     # return ret



@user_login_required
def achievement(request):
    return render(request, 'achievement.html')  # 完成

#週或日報表選擇
@user_login_required
def report(request):
    return render(request, 'report.html')


@user_login_required
def Splan(request):
    return render(request, 'StudyPlan.html')


@user_login_required
def SroomSelf(request):
    return render(request, 'Sroom-self.html')


# 多人自習室列表
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



# 開發人員頁面
def developer(request):
    return render(request, 'developer.html')

#多人自習室內部
@user_login_required
def Sroominpage(request, pk):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}studyroom/get/{pk}',
        params={'user_id': user_id},
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

#個人自習室內部更新進入時間
@user_login_required
def entry(request):
    if request.method == 'POST':

        user = request.COOKIES['user_id']

        data = {
            'user': user
        }
        r = requests.post(
            f'{root}studyroom/self/update/entrytime/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/Sroominpage-self/')
            return ret
        else:
            return redirect('/Sroominpage-self/')
            return ret

#個人自習室內部更新離開時間
@user_login_required
def exit(request):
    if request.method == 'POST':

        user_id = request.COOKIES['user_id']

        data = {
            'user_id': user_id
        }
        r = requests.post(
            f'{root}studyroom/self/update/exittime/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/studyroom-self/')
            return ret
        else:
            return redirect('/studyroom-self/')
            return ret



# 個人自習室填寫讀書資訊
@user_login_required
def Sroom_self(request):
    if request.method == 'POST':

        subject_no_id = request.POST['subject_no_id']
        settime_no_id = request.POST['settime_no_id']
        subject_detail = request.POST['subject_detail']
        user_id = request.COOKIES['user_id']

        data = {
            'user_id': user_id,
            'subject_no_id': subject_no_id,
            'settime_no_id': settime_no_id,
            'subject_detail': subject_detail,
        }
        r = requests.post(
            f'{root}studyroom/self/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/Sroominpage-self/')
            messages.success(request, '已成功')
            return ret
        else:
            messages.error(request, '失敗')
            return redirect('/Sroominpage-self/')
            return ret

    if request.method == 'GET':
        user_id = request.COOKIES['user_id']
        r = requests.get(
            f'{root}studyroom/getinfo/',
            params={'user_id': user_id},
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
# 測試的自習室內部
def test(request):
    return render(request, 'test.html')



def text(request):
    return render(request, 'text.html')


@user_login_required
def award(request):
    return render(request, 'award.html')


def Sroomtogethersub(request):
    return render(request, 'Sroom-togethersub.html')


def Splan_edit(request):
    return render(request, 'Splan_edit.html')

# 顯示此頁在現人數
def shownum(request):
    if 'num' in request.COOKIES:
        num = int(request.COOKIES['num'])
        num += 1
    else:
        num = 1
    rsp = HttpResponse('網頁瀏覽人數 = '+ str(num))
    rsp.set_cookie('num',num)
    return rsp