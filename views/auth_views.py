import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from django.contrib import messages

from django.contrib.auth.hashers import make_password

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
        # messages.success(request, '已成功登入')
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


# def ForgetPwd(request):
#     if request.method == 'GET':
#         return render(request, 'ForgetPwd.html')
#
#     user_id = request.POST['user_id']
#
#     r = requests.get(
#         f'{root}/forget/{user_id}',
#     )
#
#     result = r.json()
#     # studyrooms = result['data']
#
#     if result['success'] is True:
#         ret = redirect('/ForgetPwd/')
#         messages.success(request, '請去郵箱驗證，並重設密碼')
#         return ret
#     else:
#         messages.error(request, '查無此帳號')
#         return redirect('/ForgetPwd/')
#         return ret

# 忘記密碼及重設
def forget_pass(request):
    if request.method == 'GET':
        return render(request, 'ForgetPwd.html')

    if request.method == "POST":

        email = request.POST['email']

        data = {
            'id': email,
        }
        r = requests.post(
            f'{root}/forget/',
            data=data,
        )

        result = r.json()

        if result['success'] is True:

            import random
            from core.utls import Email

            # 产生随机8位密码
            random_password = ""
            for x in range(8):
                random_num = str(random.randint(0, 9))
                random_low_alpha = chr(random.randint(97, 122))
                random_upper_alpha = chr(random.randint(65, 90))
                random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
                random_password += random_char

            # 重置密码
            # username[0].set_password(random_password) # 會有錯誤

            # username[0].password = make_password('random_password')
            # username[0].save()

            data = {
                'id': email,
                'pwd': random_password
            }
            requests.post(
                f'{root}/forget/reset/',
                data=data,
            )

            # 发送重置密码邮件
            content_plain = "您好,您收到這封郵件,是因為你選擇了忘記密碼,因此我們為您重置了密碼,新的密碼為: %s" % random_password
            email = Email(
                smtp_server='smtp.gmail.com',
                from_addr='a10756111501@gmail.com',
                password='cgnhkebqftzilwpz',
                to_addr=email,
                type='plain',
                title='重置密碼',
                content=content_plain
            )
            flag = email.send_msg()
            # 邮件发送成功标记
            if flag == 1:
                # return render(request, 'forget_pass.html', {'success': "重置密码已发邮件"})
                ret = redirect('/login/')
                messages.success(request, '密碼已重置，請去郵箱查收')
                return ret

            # 邮件发送失败反馈
            else:
                ret = redirect('/ForgetPwd/')
                messages.success(request, '郵件發送失敗，請確認此郵箱是否存在')
                return ret
                # return render(request, 'forget_pass.html', {'send_email_failed': flag})
        else:
            messages.error(request, '查無此帳號')
            return redirect('/ForgetPwd/')
            return ret


def ForgetPwdReset(request):
    return render(request, 'ForgetPwdReset.html')
