from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.views import login_required
from django.contrib.auth import authenticate, login, logout
from.forms import UserRegisterForm

@login_required()
def home(request):
    return render(request, 'users/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                return redirect('users:home')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return redirect('users:login')
        return render(request, 'users/login.html')


@login_required()
def logout_view(request):
    logout(request)
    return JsonResponse('user logged out')

def register(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User created successfully for ' + form.cleaned_data.get('username'))
                return redirect('users:login')
        con = {'form': form}
        return render(request, 'users/register.html', con)