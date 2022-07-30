import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from django.contrib import messages

root += 'auth'

# 登入
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

# 登出
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

# 註冊
def register(request):
    return render(request, 'register.html')

    r = requests.get(
        f'{root}/register/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    studyrooms = result['data']
    return render(request, 'Sroom-together.html', {'studyrooms': studyrooms})

                            if request.method == 'GET':
                                return render(request, 'add_form.html')

    title = request.POST['title']
    name = request.POST['name']
    comment = request.POST['comment']
    data = {
        'user_id': test_user_id,
        'title': title,
        'name': name,
        'comment': comment
    }
    r = requests.post(
        f'{root}/add/',
        data=data,
    )
    result = r.json()
    return render(request, 'result.html', {'message': result['message']})