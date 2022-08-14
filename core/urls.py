"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from views import views, auth_views, discusroom_review_views, plan_review_views, report_review_views, success_review_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),

    # auth
    path('login/', auth_views.login),
    path('logout/', auth_views.logout),
    path('register/', auth_views.register),
    # path('forgetPwd/', views.forgetPwd),
    # path('register/', views.register),
    path('ForgetPwd/', auth_views.ForgetPwd),
    path('ForgetPwdReset/', auth_views.ForgetPwdReset),

    # discusroom
    # path('discusroom/', discusroom_review_views.addroom),
    path('discusroom/', discusroom_review_views.droom),
    # path('discusroom/#letmeopen/', discusroom_review_views.addroom),
    # path('discusroom/addroom_subject/', discusroom_review_views.addroom_subject),
    path('inpage/', discusroom_review_views.inpage),
    path('inpage/#letmeopen', discusroom_review_views.qus),

    # plan
    path('studyplan/', plan_review_views.Splan),

    # report
    path('report/', report_review_views.report),
    path('day-report/', report_review_views.DayReport),
    path('week-report/', report_review_views.WeekReport),

    # success
    path('achievement/', success_review_views.achievement),


    # user
    path('userdetail/', views.Udetail),
    path('edituser-detail/', views.EditUserDetail),

    # views (other)
    # studyroom
    path('studyroom/', views.sroom),
    path('studyroom-self/', views.SroomSelf),
    path('studyroom-together/', views.Sroomtogether),
    # path('studyroom-together/', views.Sserch),
    path('Sroominpage/', views.Sroominpage),
    path('Sroominpage-self/', views.Sroominpageself),

    path('developer/', views.developer),
    path('PrivacyPolicies/', views.PrivacyPolicies),
    path('award/', views.award),


    # 各類測試用
    path('day-report/', report_review_views.DayReport),
    path('week-report/', report_review_views.WeekReport),
    path('edituser-detail/', views.EditUserDetail),
    path('PrivacyPolicies/', views.PrivacyPolicies),
    path('ForgetPwd/', auth_views.ForgetPwd),
    path('ForgetPwdReset/', auth_views.ForgetPwdReset),
    path('award/', views.award),

    # 測試的自習室內部
    path('test-study/', views.test),

    # 測試用討論室內部
    path('web-chat-test/', views.WebChatTest),

    path('text/', views.text),

    # path('inner/', views.inner),
]
