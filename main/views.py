from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth.decorators import login_required
def main_view(request):
    return render(request,'views/main.html')
def home(request):
    return render(request, 'views/home.html')
def settings(request):
    return render(request, 'views/settings.html')
def orders(request):
    return render(request, 'views/orders.html')
def products(request):
    return render(request, 'views/products.html')
def customers(request):
    return render(request, 'views/customers.html')
# def login(request):
#     return render(request, 'views/login.html')


@login_required
def dashboard(request):
    return render(request, 'base/base.html')
