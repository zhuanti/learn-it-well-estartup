import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required


@user_login_required
def report(request):
    return render(request, 'report.html')  # 完成


@user_login_required
def DayReport(request):
    return render(request, 'day-report.html')


@user_login_required
def WeekReport(request):
    return render(request, 'week-report.html')

# 新增自習室資料
# @user_login_required
# def addroom(request):
#     if request.method == 'POST':
#         no = request.POST['no']
#         classroom_type_no_id = request.POST['classroom_type_no_id']
#         subject_no_id = request.POST['subject_no_id']
#         set_time = request.POST['set_time']
#         subject_detail = request.POST['subject_detail']
#
#         data = {
#             'no': no,
#             'user_id': request.COOKIES['user-id'],
#             'classroom_type_no_id': classroom_type_no_id,
#             'subject_no_id': subject_no_id,
#             'set_time': set_time,
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
#             ret = redirect('/studyroom-self')
#             messages.success(request, '新增成功')
#             return ret
#         else:
#             messages.error(request, '新增失敗')
#             return redirect('/studyroom-self')
#             return ret
