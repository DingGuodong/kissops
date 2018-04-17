# encoding: utf-8
# -*- coding: utf8 -*-
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
REDIRECT_FIELD_NAME = 'next'  # learn from django.contrib.admin.sites.login, django.contrib.auth.views.login


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/')


def management(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/admin/')


def login(request, redirect_field_name=REDIRECT_FIELD_NAME):
    redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))
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
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
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
    from django.contrib.auth.hashers import make_password
    if "can_change_password" in request.session.keys():
        if request.session['can_change_password']:
            can_change_password = True
            email = request.session.get('user_email')
    else:
        can_change_password = False

    if not can_change_password:
        return HttpResponseRedirect('/')
    else:
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        if password1 == password2:
            password = password1
        else:
            password = ""
        if password and email:
            user = User.objects.get(email=email)
            user.password = make_password(password)  # from django.contrib.auth.forms import PasswordRestForm
            user.save()
            message = {
                "error": False,
                "title": "Your password is changed successfully",
                "message": "Your password is changed successfully",
                'stage': 2
            }
        elif not email:
            message = {
                "error": True,
                "title": "Bad Request",
                "message": "Bad Request",
                'stage': 1
            }
            # TODO(Guodong Ding) redirect to /
            return render(request, 'reset_password.html', message)
        else:
            message = {
                "error": False,
                "title": "Reset your password",
                "message": "Reset your password",
                'stage': 1
            }
        return render(request, 'reset_password.html', message)


def gen_security_code(code_length=16):
    import string
    from random import sample
    # security_code_char = string.ascii_letters + string.digits + string.punctuation
    security_code_char = string.ascii_letters + string.digits
    length = code_length if code_length <= len(security_code_char) else len(security_code_char)

    return "".join(sample(security_code_char, length))


def get_user_email_by_username(username):
    user = User.objects.get(username=username)
    email = user.email
    if email:
        return email
    else:
        return


def mail_code_to_user(recipient, code, email_type='register'):
    from django.core.mail import send_mail

    if email_type == 'register':
        subject = "AdminLTE - Your security code for registration"
        message = "Your security code is \"%s\"" % code
    elif email_type == 'forget':
        subject = "AdminLTE - Your security code for password reset"
        message = "Your security code is \"%s\"" % code
    else:
        return 0
    return send_mail(
        subject,
        message,
        settings.EMAIL_FROM,
        [recipient],
        fail_silently=False,
    )


def forget_password(request):
    import time
    import datetime
    """
    Django 实现忘记密码 重置密码功能
    """

    # 如果用户没有post过数据，则初始化session
    if 'user_do_post' not in request.session.keys():
        request.session['user_try_times'] = 0  # 用户尝试提交次数
        request.session['blocked_time'] = time.time()
        request.session['blocked_times'] = 0  # 用户被屏蔽次数

    if request.method == 'POST':
        request.session['user_do_post'] = True

        # 安全治理：防范用户恶意提交
        # 安全规则：超过最大post次数后，5分钟以后再试，期间再次尝试post则刷新屏蔽时间，安全规则验证通过后则解除屏蔽
        if request.session['user_try_times'] > 5 and time.time() - request.session['blocked_time'] < datetime.timedelta(
                minutes=5).seconds:
            request.session['blocked_times'] += 1
            request.session['blocked_time'] = time.time()  # 期间再次尝试post则刷新屏蔽时间
            message = {
                'error': True,
                'title': "Max attempt times reached",
                'message': "Max attempt times reached, try later",  # TODO(Guodong Ding) time left, session expired
                'stage': 1
            }

            return render(request, 'forgot_password.html', message)

        if 'user_try_times' in request.session.keys():
            request.session['user_try_times'] += 1

        user_code = request.POST.get('security_code', "")
        if user_code:
            if user_code == request.session['security_code']:
                request.session['user_try_times'] = 0  # 重置用户尝试post次数
                request.session['blocked_times'] = 0  # 重置用户被屏蔽次数
                request.session['can_change_password'] = True
                return HttpResponseRedirect('/reset_password/')
            else:
                message = {
                    "error": True,
                    "title": "Bad security code",
                    "message": "bad security code",
                    'stage': 2
                }
                return render(request, 'forgot_password.html', message)
        username = request.POST.get('username', "")
        if username != "":
            try:
                user = User.objects.get(username=username)
                if user.username == username:
                    request.session['username'] = username
            except ObjectDoesNotExist:
                message = {
                    "error": True,
                    "title": "User not exist",
                    "message": "User not exist",
                    'stage': 1
                }
                return render(request, 'forgot_password.html', message)
        email = request.POST.get('email', "")
        if email == "":
            email = "" if username == "" else get_user_email_by_username(request.session['username'])
        else:
            try:
                User.objects.get(email=email)
            except ObjectDoesNotExist:
                email = ""
        if email:
            request.session['security_code'] = security_code = gen_security_code()
            status = mail_code_to_user(email, security_code, email_type="forget")
            if not status:
                message = {
                    "error": True,
                    "title": "Email sent failed",
                    "message": "email send failed, maybe due to bad username or email",
                    'stage': 1
                }
            else:
                request.session['user_email'] = email
                message = {
                    "error": False,
                    "title": "Email sent successfully",
                    "message": "email sent successfully, please input security code",
                    'stage': 2
                }
        elif not email:
            message = {
                "error": True,
                "title": "Email not exist",
                "message": "Email not exist",
                'stage': 1
            }
            return render(request, 'forgot_password.html', message)
        else:
            message = {
                "error": True,
                "title": "Bad request",
                "message": "bad request, input your username or email, then submit.",
                'stage': 1
            }
        return render(request, 'forgot_password.html', message)
    elif request.method == 'GET':
        message = {
            'error': False,
            'title': "Forget your password",
            'message': "input your username or email, then submit.",
            'stage': 1
        }
        return render(request, 'forgot_password.html', message)
