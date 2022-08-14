import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required


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
            f'{root}discusroom/addroom/',
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
            f'{root}discusroom/all/',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        discussrooms = result['data']
        return render(request, 'DiscusRoom.html', {'discussrooms': discussrooms})

@user_login_required
def inpage(request):
    return render(request, 'inpage.html')

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
def WebChatTest(request):
    return render(request, 'dis_test.html')
