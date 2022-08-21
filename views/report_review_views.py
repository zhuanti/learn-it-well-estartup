import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

@user_login_required
def report(request):
    return render(request, 'report.html')  # 完成

@user_login_required
def DayReport(request):
    return render(request, 'day-report.html')

@user_login_required
def WeekReport(request):
    return render(request, 'week-report.html')