import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required
from datetime import datetime

root += 'report'

#周報表
@user_login_required
def reportweek(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}/reportweek/',
        params={'user_id': user_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    inform = result['data']
    return render(request, 'ReportWeek.html', {'inform': inform})

#日報表
@user_login_required
def reportday(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}/reportday/',
        params={'user_id': user_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    inform = result['data']
    return render(request, 'ReportDay.html', {'inform': inform})

#週或日報表選擇
@user_login_required
def report(request):
    return render(request, 'report.html')  # 完成




@user_login_required
def addroom(request):
    if request.method == 'GET':
        r = requests.get(
            f'{root}/addsub/',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        subjects = result['data']
        return render(request, 'Sroominpage-self.html', {'subjects': subjects})

# 個人自習室內部
@user_login_required
def get_reviews_insideshow(request):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id'],
        r = requests.get(
            f'{root}/reporttest/',
            params={'user_id': user_id},
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        report = result['data']
        return render(request, 'Sroominpage-self.html', {'report': report})

    if request.method == 'POST':

        user = request.COOKIES['user_id']

        data = {
            'user': user
        }
        r = requests.post(
            f'{root}/studyroom/self/update/exittime/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/studyroom-self/')
            # messages.success(request, '已成功')
            return ret
        else:
            # messages.error(request, '失敗')
            return redirect('/Sroominpage-self/')
            return ret



#個人自習室更新離開時間
@user_login_required
def self_exittime(request):
    if request.method == 'POST':

        user = request.COOKIES['user_id']

        data = {
            'user': user,
        }
        r = requests.post(
            f'{root}studyroom/self/update/exittime/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/Sroominpage-self/')
            # messages.success(request, '已成功離開討論室')
            return ret

        else:
            # messages.error(request, '離開討論室')
            return redirect('/Sroominpage-self/')
            return ret

# 編輯讀書時間
@user_login_required
def report_recordtime_edit(request):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id']
        return render(request, 'Sroom-self.hml')
        entry_time = request.POST['entry_time']
        exit_time = request.POST['exit_time']

        data = {
            'user_id': request.COOKIES['user_id'],
            'entry_time': entry_time,
            'exit_time': exit_time
        }
        r = requests.post(
            f'{root}report/recordtime/',
            # params={'user_id': user_id},
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        if result['success'] is True:
            ret = redirect('/studyroom-self')
            messages.success(request, '已修改資料成功')
            return ret
        else:
            messages.error(request, '連線錯誤，請重新嘗試')
            return redirect('/')
#
#     r = requests.get(
#         f'{root}/recordtime/',
#         params={'user_id': user_id},
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     user = result['data']
#     return render(request, 'editUserDetail.html', {'user': user})
# if request.POST['pwd'] == request.POST['pwd2']:
#     entry_time = request.POST['entry_time']
#     exit_time = request.POST['exit_time']
#
#     data = {
#         'user_id': request.COOKIES['user_id'],
#         'entry_time': entry_time,
#         'exit_time': exit_time
#     }
#     r = requests.post(
#         f'{root}report/recordtime/',
#         # params={'user_id': user_id},
#         data=data,
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#
#     if result['success'] is True:
#         ret = redirect('/studyroom')
#         messages.success(request, '已修改資料成功')
#         return ret
#     else:
#         messages.error(request, '發生錯誤')
#         return redirect('/')
# else:
#     messages.error(request, '兩次所輸入密碼不同，請重新輸入')
#     return redirect('/')
#     return ret

# @user_login_required
# def get_reviews_insideshow(request):
#     user_id = request.COOKIES['user_id'],
#     r = requests.get(
#         f'{root}/inside/',
#         # params={'user_id': user_id},
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     informations = result['data']
#     return render(request, 'Sroominpage-self.html', {'informations': informations})
