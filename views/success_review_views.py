import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required
root += 'success'

@user_login_required
def achievement(request):
    if request.method == 'GET':
        r = requests.get(
            f'{root}/list/',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        success_lists = result['data']
        return render(request, 'achievement.html', {'success_lists': success_lists})