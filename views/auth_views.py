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

    # html中輸入欄位，有id=xxx，把xxx填入至後面''中的文字內
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
    requests.post(
        f'{root}/logout/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    ret = redirect('/login/')
    ret.delete_cookie('sessionid')
    ret.delete_cookie('user_id')
    messages.success(request, '已成功登出')
    return ret

# 註冊
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.POST['pass'] == request.POST['re_pass']:
        id = request.POST['email']
        name = request.POST['name']
        pwd = request.POST['pass']
        borth = request.POST.get('bir', False)
        gender = request.POST.get('gender', False)
        live = request.POST.get('live', False)

        data = {
            'id': id,
            'name': name,
            'pwd': pwd,
            'borth': borth,
            'gender': gender,
            'live': live,
            'purview': 0,
        }

        r = requests.post(
            f'{root}/register/',
            data=data,
        )

        result = r.json()

        if result['success'] is True:
            ret = redirect('/login')
            messages.success(request, '已註冊成功')
            return ret
        else:
            messages.error(request, '信箱已被註冊或是註冊時欄位格式填寫錯誤，請重新註冊')
            return redirect('/register')
            return ret

    else:
        messages.error(request, '兩次所輸入密碼不同，請重新輸入')
        return redirect('/register')
        return ret

def ForgetPwd(request):
    if request.method == 'GET':
        return render(request, 'ForgetPwd.html')

    user_id = request.POST['user_id']

    r = requests.get(
        f'{root}/forget/{user_id}',
    )

    result = r.json()
    # studyrooms = result['data']

    if result['success'] is True:
        ret = redirect('/ForgetPwd/')
        messages.success(request, '請去郵箱驗證，並重設密碼')
        return ret
    else:
        messages.error(request, '查無此帳號')
        return redirect('/ForgetPwd/')
        return ret

def ForgetPwdReset(request):
    return render(request, 'ForgetPwdReset.html')

