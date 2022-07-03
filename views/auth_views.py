import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from django.contrib import messages

root += 'auth'

def login(request):
    # return render(request, 'login.html')

    # 設置若已經登入過，所導向的畫面
    if 'user_id' in request.COOKIES:
        messages.success(request, '已成功登入')
        return redirect('/')

    if request.method == 'GET':
        return render(request, 'login.html')

    user_id = request.POST['your_name']
    pwd = request.POST['your_pass']

    data = {
        'id': user_id,
        'pwd': pwd

    }

    r = requests.post(
        f'{root}/login/',
        data=data
    )

    result = r.json()

    if result['success'] is True:
        ret = redirect('/')
        ret.set_cookie('sessionid', result['sessionid'])
        # ret.set_cookie('sessionid', result['sessionid'], max_age=60 * 60) 登入時間
        ret.set_cookie('user_id', user_id)
        messages.success(request, '已成功登入')
        return ret
    else:
        messages.error(request, '帳號或密碼錯誤')
        return redirect('/login/')

def logout(request):
    r = requests.post(
        f'{root}/logout/',
        cookies = {'sessionid': request.COOKIES['sessionid']}
    )

    ret = redirect('/login/')
    ret.delete_cookie('sessionid')
    ret.delete_cookie('user_id')
    messages.success(request, '已成功登出')
    return ret