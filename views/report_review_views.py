import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

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
    user = result['data']
    return render(request, 'ReportWeek.html', {'user': user})

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
    user = result['data']
    return render(request, 'ReportDay.html', {'user': user})


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


# @user_login_required
# def addroom(request):
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

# 顯示個人資料
# @user_login_required
# def Udetail(request):
#     user_id = request.COOKIES['user_id'],
#     r = requests.get(
#         f'{root}user/detail/',
#         params={'user_id': user_id},
#         # 'user_id': request.COOKIES['user_id'],
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     user = result['data']
#     return render(request, 'UserDetail.html', {'user': user})
@user_login_required
def get_reviews_insideshow(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}/reporttest/',
        params={'user_id': user_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    report = result['data']
    # print(report)
    return render(request, 'Sroominpage-self.html', {'report': report})



    # user_id = request.COOKIES['user_id'],
    # r = requests.get(
    #     f'{root}/inside/',
    #     params={'user_id': user_id},
    #     # 'user_id': request.COOKIES['user_id'],
    #     cookies={'sessionid': request.COOKIES['sessionid']}
    # )
    # result = r.json()
    # informations = result['data']
    # return render(request, 'Sroominpage-self.html', {'informations': informations})


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
            messages.error(request, '發生錯誤')
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
