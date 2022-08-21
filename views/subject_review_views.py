# import requests
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from core.settings import API_URL as root
# from utils.decorators import user_login_required
#
# root += 'subject'
#
#
# @user_login_required
# def get_all_reviews(request):
#     if request.method == 'GET':
#         r = requests.get(
#             f'{root}/all/',
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         subjects = result['data']
#         return render(request, 'Sroom-self.html', {'subjects': subjects})
