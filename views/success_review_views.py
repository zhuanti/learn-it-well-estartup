import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required
root += 'success'

@user_login_required
def achievement(request):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id'],
        r = requests.get(
            f'{root}/list/',
            params={'user_id': user_id},
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        sus_all = result['data']

        return render(request, 'achievement.html', {'sus_alls': sus_all})

@user_login_required
def achievementup(request, pk):
    if request.method == 'POST':

        no = pk
        user_id = request.COOKIES['user_id']

        data = {
            'user_id': user_id,
            'no': no,
        }
        r = requests.post(
            f'{root}/list/update/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/achievement/')
            return ret
        else:
            ret = redirect('/achievement/')
            return ret
