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

from django.contrib.auth import views as dj_auth_views

from views import views, auth_views, subject_review_views, discusroom_review_views, \
    plan_review_views, report_review_views, success_review_views, \
    user_review_views, settime_review_views
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    # auth
    path('login/', auth_views.login),
    path('logout/', auth_views.logout),
    path('register/', auth_views.register),
    # path('ForgetPwd/', auth_views.ForgetPwd),

    path('ForgetPwd/', auth_views.forget_pass, name="forget_pass"),
    path('ForgetPwdReset/', auth_views.ForgetPwdReset),

    # discusroom
    path('discusroom/', discusroom_review_views.droom),
    path('inpage/<int:pk>/', discusroom_review_views.inpage),
    path('dis_test/', discusroom_review_views.WebChatTest),
    path('discusroom/search/', discusroom_review_views.search),

    path('addqus/<int:pk>/', discusroom_review_views.addqus), # 問題
    path('addans/<int:pk>/', discusroom_review_views.addans),

    # plan
    path('studyplan/', plan_review_views.Splan),

    # report
    path('report/', report_review_views.report),
    path('day-report/', report_review_views.DayReport),
    path('week-report/', report_review_views.WeekReport),

    # success
    path('achievement/', success_review_views.achievement),

    # user
    path('userdetail/', user_review_views.Udetail),
    path('edituser-detail/', user_review_views.EditUserDetail),

    # views (other)
    # studyroom
    path('studyroom/', views.sroom),
    # path('studyroom-self/', settime_review_views.get_selfall_reviews),
    path('studyroom-self/', views.Sroom_self),
    # path('studyroom-self/', views.SroomSelf),
    path('studyroom-together/', views.Sroomtogether),
    path('studyroom-togethersub/<int:pk>/', subject_review_views.get_togall_reviews),
    path('studyroom/Sserch/', views.Sserch),

    # path('studyroom-together/', views.Sserch),
    # path('Sroominpage/', views.Sroominpage),
    path('Sroominpage/<int:pk>/', views.Sroominpage),
    path('Sroominpage-self/', report_review_views.get_reviews_insideshow),

    path('developer/', views.developer),
    path('PrivacyPolicies/', views.PrivacyPolicies),

    # 各類測試用
    # 測試的自習室內部
    path('test-study/', views.test),

    # 測試的獎勵頁面
    path('award/', views.award),
    # 測試用討論室內部
    # path('web-chat-test/', discusroom_review_views.WebChatTest),

    path('text/', views.text),
    path('ReportWeek/', report_review_views.reportweek),
    path('ReportDay/', report_review_views.reportday),

    path('studyplan_edit/', views.Splan_edit),

    # path('day-report/', report_review_views.DayReport),
    # path('week-report/', report_review_views.WeekReport),

    # path('edituser-detail/', user_review_views.EditUserDetail),

    # path('PrivacyPolicies/', views.PrivacyPolicies),

    # path('ForgetPwd/', auth_views.ForgetPwd),
    # path('ForgetPwdReset/', auth_views.ForgetPwdReset),

    # path('inner/', views.inner),
]
