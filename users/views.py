from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
# Create your views here.

def login_view(request):
    return render(request, 'assets/login.html')