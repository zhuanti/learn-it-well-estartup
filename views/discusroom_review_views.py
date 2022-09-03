import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

root += 'discusroom'

@user_login_required
def droom(request):

    if request.method == 'POST':
        no = request.POST['ano']
        subject_no_id = request.POST['asubject_no']
        name = request.POST['aname']
        total_people = request.POST['atotal_people']

        data = {
            'no': no,
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
    r = requests.get(
        f'{root}/get/{pk}',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    if result['success'] is True:
        discussroom = result['data']
        # return render(request, 'inpage.html', {'discussroom': discussroom})
        return render(request, 'inpageT.html', {'discussroom': discussroom})
    else:
        messages.error(request, '查無此房間')
        return redirect('/discusroom/')
        return ret

        # message = result['message']
        # return render(request, 'inpage.html', {'message': message})


# 問題列表
@user_login_required
def qus(request):
    r = requests.get(
        f'{root}discusroom/qus/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    discussroom_questions = result['data']
    return render(request, 'inpage.html', {'discussroom_questions': discussroom_questions})

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


