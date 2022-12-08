import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required
root += 'success'

@user_login_required
def achievement(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}/list/',
        params={'user_id': user_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    sus_all = result['data']

    return render(request, 'achievement.html', {'sus_alls':sus_all})