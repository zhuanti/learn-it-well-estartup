import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

# 顯示個人資料
@user_login_required
def Udetail(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}user/detail/',
        params={'user_id': user_id},
        # 'user_id': request.COOKIES['user_id'],
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    user = result['data']
    return render(request, 'UserDetail.html', {'user': user})

# 編輯個人資料(修改版)
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

    name = request.POST['name']
    live = request.POST['live']
    borth = request.POST['borth']

    data = {
        'user_id': request.COOKIES['user_id'],
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

# @user_login_required
# def EditUserDetail(request):
#     if request.method == 'GET':
#         user_id = request.COOKIES['user_id']
#         r = requests.get(
#             f'{root}user/detail/',
#             params={'user_id': user_id},
#             # 'user_id': request.COOKIES['user_id'],
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         user = result['data']
#         return render(request, 'editUserDetail.html', {'user': user})
#
#     id = request.POST.get['user.id']
#     name = request.POST.get['user.name']
#     live = request.POST.get['user.live']
#     borth = request.POST.get['user.borth']
#
#     data = {
#         'id': id,
#         'name': name,
#         'live': live,
#         'borth': borth
#     }
#
#     user_id = request.COOKIES['user_id']
#     r = requests.post(
#         f'{root}user/detail/edit/',
#         params={'user_id': user_id},
#         cookies={'sessionid': request.COOKIES['sessionid']},
#         data=data
#     )
#     result = r.json()
#     user = result['data']
#     return render(request, 'UserDetail.html', {'user': user})

    # user_id = request.COOKIES['user_id'],
    # r = requests.get(
    #    f'{root}user/detail/edit/',
    #    params={'user_id': user_id},
    #    # 'user_id': request.COOKIES['user_id'],
    #    cookies={'sessionid': request.COOKIES['sessionid']}
    # )
    # result = r.json()
    # user = result['data']
    # return render(request, 'editUserDetail.html', {'user': user})