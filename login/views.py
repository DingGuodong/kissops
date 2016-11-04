from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='UserName:', max_length=50)
    password = forms.CharField(label='Password:', max_length=50, widget=forms.PasswordInput)


# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    return render_to_response('index.html', {'username': username})


def _login(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            if username is not None and password is not None:
                user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, '_login.html', {'loginForm': loginForm, 'login_error': 'error!'})
    else:
        loginForm = LoginForm()
        return render(request, '_login.html', {'loginForm': loginForm})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username is not None and password is not None:
            user = auth.authenticate(username=username, password=password)
        elif email is not None and password is not None:
            try:
                username = User.objects.get(email=email)
            except User.DoesNotExist:
                return render(request, 'login.html', {'loginFailed': True})
            user = auth.authenticate(username=username, password=password)
        else:
            return render(request, 'login.html', {'loginFailed': True})
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'loginFailed': True})
    elif request.method == 'GET'and request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
