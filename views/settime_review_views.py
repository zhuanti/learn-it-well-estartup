# import requests
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from core.settings import API_URL as root
# from utils.decorators import user_login_required
#
# root += 'settime'
#
#
# @user_login_required
# def get_selfall_reviews(request):
#     if request.method == 'GET':
#         r = requests.get(
#             f'{root}/selfall/',
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         settimes = result['data']
#         return render(request, 'Sroom-self.html', {'settimes': settimes})

# @user_login_required
# def get_togall_reviews(request, pk):
#     if request.method == 'GET':
#         r = requests.get(
#             f'{root}/all/{pk}',
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         studyroom = result['data']
#         return render(request, 'Sroom-togethersub.html', {'studyroom': studyroom})
