# from django.shortcuts import redirect
#
# def user_login_required(function):
#     def wrapper(request, *args, **kw):
#         if 'sessionid' not in request.COOKIES.KEY():
#             return redirect('/login/')
#         else:
#             # 指所有api_views
#             return function(request, *args, **kw)
#     return wrapper

from django.shortcuts import render, redirect


def user_login_required(function):
    def wrapper(request, *args, **kw):
        if 'sessionid' not in request.COOKIES.keys():
            return redirect('/login/')
        else:
            return function(request, *args, **kw)
    return wrapper