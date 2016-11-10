from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/')


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
    elif request.method == 'GET' and request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def register(request):
    from django.contrib.auth.forms import UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.email = request.POST.get('email')  # this is not work.
            form.save()
            if request.POST.get('username') is not None and request.POST.get('email') is not None:
                User.objects.filter(username=request.POST.get('username')).update(email=request.POST.get('email'))
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'register.html', {'formFailed': True})
    else:
        return render(request, 'register.html')


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    return render_to_response('profile.html', {'username': username})
