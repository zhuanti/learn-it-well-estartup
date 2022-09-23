import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required


@user_login_required
def Splan(request):
    return render(request, 'StudyPlan.html')


# 新增
# @user_login_required
# def addplan(request):
#     if request.method == 'GET':
#         return render(request, 'StudyPlan.html')
#
#         # no = request.POST['no']
#         name = request.POST['name']
#         pace = request.POST[0]
#         datetime = request.POST['datetime']
#         data = {
#             # 'no': no,
#             'user_id': request.COOKIES['user_id'],
#             'name': name,
#             'pace': pace,
#             'datetime': datetime,
#         }
#     r = requests.post(
#         f'{root}/add/',
#         data=data,
#     )
#     result = r.json()
#     return render(request, 'StudyPlan.html', {'message': result['message']})

#顯示
# @user_login_required
# def get_all_reviews_test(request):
#     user_id = request.COOKIES['user_id'],
#     r = requests.get(
#         f'{root}/get/',
#         params={'user_id': user_id},
#         # 'user_id': request.COOKIES['user_id'],
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     plans = result['data']
#     return render(request, 'StudyPlan.html', {'plans': plans})
