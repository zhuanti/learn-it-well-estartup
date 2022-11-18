import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required


# @user_login_required
# def Splan(request):
#     return render(request, 'StudyPlan.html')


# @user_login_required
# def plan(request):
#     if request.method == 'POST':
#         user_id = request.COOKIES['user_id']
#         name = request.POST['name']
#         pace = request.POST[0]
#         # datetime = request.POST['datatime']
#
#         data = {
#             'user_id': request.COOKIES['user_id'],
#             'name': name,
#             'pace': pace,
#             # 'datetime': datime,
#         }
#
#         r = requests.post(
#             f'{root}/add/',
#             data=data,
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         return render(request, 'StudyPlan.html')
#
#
# @user_login_required
# def get_all_reviews_test(request):
#     user_id = request.COOKIES['user_id'],
#     r = requests.get(
#         f'{root}/get/',
#         params={'user_id': user_id},
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     plans = result['data']
#     # print(plans)
#     return render(request, 'StudyPlan.html', {'plans': plans})

# if result['success'] is True:
#     # ret = redirect('/studyplan')
#     messages.success(request, '已新增成功')
#     # return ret
#     return render(request, 'StudyPlan.html')
# else:
#     messages.error(request, '新增失敗')
#     # return redirect('/studyplan')
#     # return ret
#     return render(request, 'StudyPlan.html')

# 新增
# @user_login_required
# def addplan(request):
#     if request.method == 'GET':
#         return render(request, 'StudyPlan.html')
#
#         # no = request.POST['no']
#         name = request.POST['name']
#         pace = request.POST[0]
#         datetime = request.POST['datetime']
#         data = {
#             # 'no': no,
#             'user_id': request.COOKIES['user_id'],
#             'name': name,
#             'pace': pace,
#             'datetime': datetime,
#         }
#     r = requests.post(
#         f'{root}/add/',
#         data=data,
#     )
#     result = r.json()
#     return render(request, 'StudyPlan.html', {'message': result['message']})

# 顯示讀書規劃(舊的)
# @user_login_required
# def get_all_reviews_test(request):
#     user_id = request.COOKIES['user_id'],
#     r = requests.get(
#         f'{root}plan/get/',
#         params={'user_id': user_id},
#         # 'user_id': request.COOKIES['user_id'],
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     plans = result['data']
#     return render(request, 'StudyPlan.html', {'plans': plans})

# 顯示讀書規劃
@user_login_required
def get_all_reviews_test(request):
    user_id = request.COOKIES['user_id'],
    r = requests.get(
        f'{root}plan/get/',
        params={'user_id': user_id},
        # 'user_id': request.COOKIES['user_id'],
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    plans = result['data']
    return render(request, 'StudyPlan.html', {'plans': plans})

    # if request.method == 'POST':
    #
    #     no = request.POST['no']
    #     data = {
    #         'user_id': request.COOKIES['user_id']
    #     }
    #
    #     r = requests.post(
    #         f'{root}/delete/{no}/',
    #         data=data,
    #         cookies={'sessionid': request.COOKIES['sessionid']}
    #     )

    # user_id = request.COOKIES['user_id'],
    # r = requests.get(
    #    f'{root}/get/',
    #    params={'user_id': user_id},
    # 'user_id': request.COOKIES['user_id'],
    #    cookies={'sessionid': request.COOKIES['sessionid']}
    # )
    # result = r.json()
    # plans = result['data']
    # return render(request, 'StudyPlan.html', {'plans': plans})


# #新增讀書規劃(舊的)
# @user_login_required
# def addplans(request):
#     if request.method == 'GET':
#         user_id = request.COOKIES['user_id'],
#         r = requests.get(
#             f'{root}plan/get/',
#             params={'user_id': user_id},
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#         plans = result['data']
#         return render(request, 'Splan_add.html', {'plans': plans})
#
#     if request.method == 'POST':
#         name = request.POST.get('plans_name')
#         user_id = request.COOKIES['user_id']
#
#         data = {
#             'user_id': user_id,
#             'name': name,
#             'datetime': "",
#         }
#         r = requests.post(
#             f'{root}plan/add/',
#             data=data,
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#
#         if result['success'] is True:
#             ret = redirect('/studyplan')
#             messages.success(request, '已新增規劃成功')
#             return ret
#         else:
#             messages.error(request, '新增規劃失敗')
#             return redirect('/studyplan')
#             return ret

# 新增讀書規劃
@user_login_required
def addplans(request):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id'],
        r = requests.get(
            f'{root}plan/get/',
            params={'user_id': user_id},
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        plans = result['data']
        return render(request, 'Splan_add.html', {'plans': plans})

    if request.method == 'POST':
        name = request.POST.get('plans_name')
        user_id = request.COOKIES['user_id']

        data = {
            'user_id': user_id,
            'name': name,
            'datetime': "",
        }
        r = requests.post(
            f'{root}plan/add/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            ret = redirect('/studyplan')
            messages.success(request, '已新增規劃成功')
            return ret
        else:
            messages.error(request, '新增規劃失敗')
            return redirect('/studyplan')
            return ret


# #編輯讀書規劃(舊的)
# @user_login_required
# def editplans(request, pk):
#     if request.method == 'GET':
#         user_id = request.COOKIES['user_id']
#         r = requests.get(
#             f'{root}plan/showedit/',
#             params={'no': pk, 'user_id': user_id},
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#
#         if result['success'] is True:
#             plan = result['data']
#             return render(request, 'Splan_edit.html', {'plan': plan})
#         else:
#             messages.error(request, '查無此規劃')
#             return redirect('/studyplan')
#             return ret
#
#
#
#     if request.method == 'POST':
#         name = request.POST['name']
#
#         data = {
#             'no': pk,
#             'name': name
#         }
#         r = requests.post(
#             f'{root}plan/editplan/',
#             data=data,
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         result = r.json()
#
#         if result['success'] is True:
#             messages.error(request, '修改規劃成功')
#             return redirect('/studyplan')
#             return ret
#         else:
#             messages.error(request, '修改規畫失敗')
#             return redirect('/studyplan')
#             return ret


# 編輯讀書規劃
@user_login_required
def editplans(request, pk):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id']
        r = requests.get(
            f'{root}plan/showedit/',
            params={'no': pk, 'user_id': user_id},
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            plan = result['data']
            return render(request, 'Splan_edit.html', {'plan': plan})
        else:
            messages.error(request, '查無此規劃')
            return redirect('/studyplan')
            return ret

    if request.method == 'POST':
        name = request.POST['name']

        data = {
            'no': pk,
            'name': name
        }
        r = requests.post(
            f'{root}plan/editplan/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()

        if result['success'] is True:
            messages.error(request, '修改規劃成功')
            return redirect('/studyplan')
            return ret
        else:
            messages.error(request, '修改規畫失敗')
            return redirect('/studyplan')
            return ret


@user_login_required
def deleteplans(request, pk):
    if request.method == 'GET':
        user_id = request.COOKIES['user_id'],
        r = requests.get(
            f'{root}plan/showedit/',
            params={'no': pk, 'user_id': user_id},
            # 'user_id': request.COOKIES['user_id'],
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        if result['success'] is True:
            plan = result['data']
            return render(request, 'Splan_del.html', {'plan': plan})
        else:
            messages.error(request, '查無此規劃')
            return redirect('/studyplan')
            return ret

    if request.method == 'POST':
        name = request.POST['name']

        data = {
            'no': pk,
            'name': name
        }
        r = requests.post(
            f'{root}plan/delete/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        result = r.json()
        if result['success'] is True:
            messages.error(request, '刪除規劃成功')
            return redirect('/studyplan')
            return ret
        else:
            messages.error(request, '刪除規畫失敗')
            return redirect('/studyplan')
            return ret
