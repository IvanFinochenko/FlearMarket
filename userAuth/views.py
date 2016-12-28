from django.shortcuts import render, redirect
from django.conf.urls import include
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from userAuth import templates

def login(request):
    args={}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/market/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/market/')

def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newUser_form = UserCreationForm(request.POST)
        if newUser_form.is_valid():
            newUser_form.save()
            newUser = auth.authenticate(username=newUser_form.cleaned_data['username'], password=newUser_form.cleaned_data['password2'])
            auth.login(request, newUser)
            return redirect('/market/')
        else:
            args['form'] = newUser_form
    return render(request, 'register.html', args)





