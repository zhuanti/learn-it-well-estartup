import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

root += 'subject'


@user_login_required
def get_selfall_reviews(request):
    if request.method == 'GET':
        r = requests.get(
            f'{root}/selfall/',
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        subjects = result['data']
        return render(request, 'Sroom-self.html', {'subjects': subjects})

@user_login_required
def get_togall_reviews(request, pk):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id']
        r = requests.get(
            f'{root}/all/{pk}',
            params={'user_id': user_id},
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        studyroom = result['data']
        return render(request, 'Sroom-togethersub.html', {'studyroom': studyroom})

    if request.method == 'POST':

        user_id = request.COOKIES['user_id']
        subject_no_id = request.POST['subject_no_id']
        settime_no_id = request.POST['settime_no_id']
        subject_detail = request.POST['subject_detail']

        data = {
            'user_id': user_id,
            'subject_no_id': subject_no_id,
            'settime_no_id': settime_no_id,
            'subject_detail': subject_detail,
        }
        r = requests.post(
            f'{root}subject/studyroom/many/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/Sroominpage/<int:pk>/')
            messages.success(request, '已新增問題成功')
            return ret
        else:
            messages.error(request, '新增問題失敗')
            return redirect('/Sroominpage/<int:pk>//')
            return ret



