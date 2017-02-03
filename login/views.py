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


def management(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/admin/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username and password:
            user = auth.authenticate(username=username, password=password)
        elif email and password:
            try:
                username = User.objects.get(email=email)
            except User.DoesNotExist:
                return render(request, 'login.html', {'loginFailed': True})
            user = auth.authenticate(username=username, password=password)
        else:
            return render(request, 'login.html', {'loginFailed': True})
        if user and user.is_active:
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
    content = dict()
    if request.user.is_authenticated():
        auth.logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        if email in [user.email for user in User.objects.all()]:
            content['formFailed'] = True
            content['errorMessage'] = "Email %s is already registered!" % email
            return render(request, 'register.html', context=content)
        if not request.POST.get('agree'):
            content['formFailed'] = True
            content['errorMessage'] = "You must accept agreement!"
            return render(request, 'register.html', context=content)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if username and email:
                User.objects.filter(username=username).update(email=email)
            return HttpResponseRedirect('/')
        else:
            content['formFailed'] = True
            content['errorMessage'] = form.errors
            print form.errors
            return render(request, 'register.html', context=content)
    else:
        return render(request, 'register.html', context=content)


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    return render_to_response('profile.html', {'username': username})


def reset_password(request):
    pass
