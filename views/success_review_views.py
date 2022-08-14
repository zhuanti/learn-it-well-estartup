import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

@user_login_required
def achievement(request):
    return render(request, 'achievement.html')  # 完成