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

from views import views, auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    # path('front/', views.beforelogin_index), # 登入前的首頁畫面
    path('login/', auth_views.login),
    path('logout/', auth_views.logout),
    path('register/', auth_views.register),

    path('inner/', views.inner),
    # path('forgetPwd/', views.forgetPwd),
    path('userdetail/', views.Udetail),
    path('studyroom/', views.sroom),
    path('discusroom/', views.droom),
    path('achievement/', views.achievement),
    path('report/', views.report),
    path('studyplan/', views.Splan),
    path('studyroom-self/', views.SroomSelf),
    path('studyroom-together/', views.Sroomtogether),
    # path('register/', views.register),
    # path('developers/', views.beforelogin_developer), # 登入前開發人員頁面
    path('developer/', views.developer),
    path('inpage/', views.inpage),
    path('Sroominpage/', views.Sroominpage),
    path('Sroominpage-self/', views.Sroominpageself),
    path('day-report/', views.DayReport),
    path('week-report/', views.WeekReport),
    path('edit user-detail/', views.EditUserDetail),
    path('PrivacyPolicies/', views.PrivacyPolicies),
    path('ForgetPwd/', views.ForgetPwd),
    path('ForgetPwdReset/', views.ForgetPwdReset),

    # 測試的自習室內部
    path('test-study/', views.test),

    # 測試用討論室內部
    path('web-chat-test/', views.WebChatTest),
]
