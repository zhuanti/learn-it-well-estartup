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
    path('discusroom/adduinfo/<int:pk>/', discusroom_review_views.adduinfo), # 寫資訊到報表
    path('discusroom/addLeave/', discusroom_review_views.addLeave), # 新增離開時間
    path('inpage/<int:pk>/', discusroom_review_views.inpage),
    path('dis_test/', discusroom_review_views.WebChatTest),
    path('discusroom/search/', discusroom_review_views.search),

    path('addqus/<int:pk>/', discusroom_review_views.addqus),  # 問題
    path('addans/<int:pk>/', discusroom_review_views.addans),  # 答案

    # plan
    path('studyplan/', plan_review_views.get_all_reviews_test),  # 讀書規劃顯示
    path('plansadd/', plan_review_views.addplans),  # 讀書規劃新增
    path('edit/<int:pk>/', plan_review_views.editplans),  # 讀書規劃編輯
    path('delete/<int:pk>/', plan_review_views.deleteplans),

    # report
    path('report/', report_review_views.report),  # 選擇週或日報表
    path('ReportWeek/', report_review_views.reportweek),  # 週報表
    path('ReportDay/', report_review_views.reportday),  # 日報表

    # success
    path('achievement/', success_review_views.achievement),
    path('achievement/update/<int:pk>/', success_review_views.achievementup),

    # user
    path('userdetail/', user_review_views.Udetail),  # 使用者個人資訊
    path('edituser-detail/', user_review_views.EditUserDetail),  # 使用者個人資訊編輯

    # views (other)
    # studyroom
    path('studyroom/', views.sroom),  # 自習室個人或多人選擇
    path('studyroom-self/', views.Sroom_self),  # 個人自習室填寫讀書資訊
    path('studyroom-together/', views.Sroomtogether),  # 多人自習室列表
    path('studyroom-togethersub/<int:pk>/', subject_review_views.get_togall_reviews),  # 多人自習室填寫讀書資訊
    path('studyroom/Sserch/', views.Sserch),

    # path('studyroom-together/', views.Sserch),
    path('Sroominpage/<int:pk>/', views.Sroominpage),  # 多人自習室內部
    path('Sroominpage-self/', report_review_views.get_reviews_insideshow),  # 個人自習室內部
    path('Sroominpage-self/entry/', views.entry),
    path('Sroominpage-self/exit/', views.exit),
    path('Sroominpage/exit/<int:pk>/', subject_review_views.exit),

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

    path('studyplan_edit/', views.Splan_edit),

    # path('shownum/', views.showcnum),
    # path('day-report/', report_review_views.DayReport),
    # path('week-report/', report_review_views.WeekReport),

    # path('edituser-detail/', user_review_views.EditUserDetail),

    # path('PrivacyPolicies/', views.PrivacyPolicies),

    # path('ForgetPwd/', auth_views.ForgetPwd),
    # path('ForgetPwdReset/', auth_views.ForgetPwdReset),

    # path('inner/', views.inner),
]
