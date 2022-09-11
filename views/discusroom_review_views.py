import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

root += 'discusroom'


@user_login_required
def droom(request):
    if request.method == 'POST':
        # no = request.POST['ano']
        subject_no_id = request.POST['asubject_no']
        name = request.POST['aname']
        total_people = request.POST['atotal_people']

        data = {
            # 'no': no,
            'subject_no_id': subject_no_id,
            'name': name,
            'total_people': total_people,
        }

        r = requests.post(
            f'{root}/addroom/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        # subjects = result['data']
        # return render(request, 'DiscusRoom.html', {'subjects': subjects})

        if result['success'] is True:
            ret = redirect('/discusroom')
            messages.success(request, '已新增房間成功')
            return ret
        else:
            messages.error(request, '新增房間失敗')
            return redirect('/discusroom')
            return ret

    if request.method == 'GET':
        r = requests.get(
            f'{root}/all/',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        discussrooms = result['data']
        return render(request, 'DiscusRoom.html', {'discussrooms': discussrooms})


@user_login_required
def search(request):
    name = request.GET.get('name')
    r = requests.get(
        f'{root}/get_critic_reviews/',
        params={'name': name},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    data = r.json()
    discussrooms = data['data']
    return render(request, 'DiscusRoom.html', {'discussrooms': discussrooms})


@user_login_required
def inpage(request, pk):
    if request.method == 'GET':
        r = requests.get(
            f'{root}/get/{pk}',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        discussroom = result['data']
        return render(request, 'inpage.html', {'discussroom': discussroom})
        # if result['success'] is True:
        #     discussroom = result['data']
        #     return render(request, 'inpage.html', {'discussroom': discussroom})
        #     # return render(request, 'inpageT.html', {'discussroom': discussroom})
        # else:
        #     messages.error(request, '查無此房間')
        #     return redirect('/discusroom/')
        #     return ret
    if request.method == 'POST':
        no = request.POST['no']
        discussroom_no_id = request.POST['discussroom_no_id']
        title = request.POST['title']
        quser_id = request.POST['quser_id']
        datetime = request.POST['datetime']

        data = {
            'no': no,
            'discussroom_no_id': discussroom_no_id,
            'title': title,
            'quser_id': quser_id,
            'datetime': datetime,
        }

        r = requests.post(
            f'{root}/qus/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        if result['success'] is True:
            ret = redirect('/inpage')
            messages.success(request, '新增問題成功')
            return ret
        else:
            messages.error(request, '新增問題失敗')
            return redirect('/inpage')
            return ret

    # message = result['message']
    # return render(request, 'inpage.html', {'message': message})


# 問題列表
@user_login_required
def qus(request):
    r = requests.get(
        f'{root}discusroom/get/<int:pk>',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    discussroom_questions = result['data']
    return render(request, 'inpage.html', {'discussroom_questions': discussroom_questions})


# 提問寫入
@user_login_required
def get_togall_reviews(request, pk):
    if request.method == 'GET':
        r = requests.get(
            f'{root}/get/{pk}',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        discussroom = result['data']
        return render(request, 'inpage.html', {'discussroom': discussroom})
    if request.method == 'POST':
        no = request.POST['no']
        discussroom_no_id = request.POST['discussroom_no_id']
        title = request.POST['title']
        quser_id = request.POST['quser_id']
        datetime = request.POST['datetime']

        data = {
            'no': no,
            'discussroom_no_id': discussroom_no_id,
            'title': title,
            'quser_id': quser_id,
            'datetime': datetime,
        }

        r = requests.post(
            f'{root}/qus/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        if result['success'] is True:
            ret = redirect('/inpage')
            messages.success(request, '新增問題成功')
            return ret
        else:
            messages.error(request, '新增問題失敗')
            return redirect('/inpage')
            return ret


# 測試用討論室內部
@user_login_required
def WebChatTest(request):
    r = requests.get(
        f'{root}discusroom/getuser/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    result = r.json()
    if result['success'] is True:
        ret = redirect('/dis_test')
        # messages.success(request, '已新增房間成功')
        return ret
    else:
        messages.error(request, '查無此人')
        return redirect('/dis_test')
        return ret
    users = result['data']
    return render(request, 'dis_test.html', {'users': users})
    # return render(request, 'dis_test.html')
