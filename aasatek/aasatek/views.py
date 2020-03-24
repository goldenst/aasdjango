from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth import authenticate, login, get_user_model

from .forms import LoginForm, RegisterForm

User = get_user_model()

def home_page(request):
    context = {
        'title': "Welcone to aas"
    }
    return render(request, 'layout/landing.html', context)


def navar(request):
    return render(request, 'layout/header.html', {})

# ------------- LOGIN page --------------------


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    # print(request.user.is_authenticated)
    if form.is_valid():
        # print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            context['form'] = LoginForm()
            return redirect('/')
        else:
            print('error')
    return render(request, 'auth/login.html', context)

# --------------- Register Page------------------------


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'auth/register.html', context)
