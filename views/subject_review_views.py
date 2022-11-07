import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

root += 'subject'


# 多人讀書資料填寫(抓科目時間、以及房間，新增填寫資料)
@user_login_required
def get_togall_reviews(request, pk):
    if request.method == 'POST':

        subject_no_id = request.POST['subject_no_id']
        settime_no_id = request.POST['settime_no_id']
        subject_detail = request.POST['subject_detail']
        user_id = request.COOKIES['user_id']

        data = {
            'user_id': user_id,
            'subject_no_id': subject_no_id,
            'settime_no_id': settime_no_id,
            'subject_detail': subject_detail,
        }
        r = requests.post(
            f'{root}/studyroom/many/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect(f'/Sroominpage/{pk}')
            messages.success(request, '已成功')
            return ret
        else:
            messages.error(request, '失敗')
            return redirect('/studyroom-together/')
            return ret

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



