from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            # Perform login
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            print(username)
            print(password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'You logged in as {username} !!')
                return redirect('home')
            else:
               messages.error(request,f'Invalid username or password')
        else:
            messages.error(request,f'Invalid username or password')
    elif request.method=='GET':
        login_form = AuthenticationForm()
    return render(request, 'assets/login.html',{'login_form':login_form})