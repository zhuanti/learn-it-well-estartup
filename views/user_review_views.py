import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required


# 顯示使用者個人資料
@user_login_required
def Udetail(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}user/detail/',
        params={'user_id': user_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    user = result['data']
    return render(request, 'UserDetail.html', {'user': user})


# 編輯使用者個人資料
@user_login_required
def EditUserDetail(request):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id']
        r = requests.get(
            f'{root}user/detail/',
            params={'user_id': user_id},
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        user = result['data']
        return render(request, 'editUserDetail.html', {'user': user})

    if request.POST['pwd'] == request.POST['pwd2']:
        pwd = request.POST['pwd']
        name = request.POST['name']
        live = request.POST['live']
        borth = request.POST['borth']

        data = {
            'user_id': request.COOKIES['user_id'],
            'pwd': pwd,
            'name': name,
            'live': live,
            'borth': borth
        }
        r = requests.post(
            f'{root}user/detail/edit/',
            # params={'user_id': user_id},
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/userdetail')
            messages.success(request, '已修改資料成功')
            return ret
        else:
            messages.error(request, '生日格式填寫錯誤，請重新修改')
            return redirect('/edituser-detail')
    else:
        messages.error(request, '兩次所輸入密碼不同，請重新輸入')
        return redirect('/edituser-detail')
        return ret
