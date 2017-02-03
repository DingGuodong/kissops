from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Hosts
from django import forms


# Create your views here.
def database_error(request, message):
    if message == '' or message is None:
        message = 'Error detail is not given.'
    context = {
        'database_error': message,
    }
    return render(request, 'exception/error.html', context)


def database_error_decorator(func):
    from functools import wraps
    from django.utils.decorators import available_attrs

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            try:
                return view_func(request, *args, **kwargs)
            except Exception as e:
                return database_error(request, message=e.message)

        return _wrapped_view

    return decorator(func)


@database_error_decorator
@login_required(login_url='/login/')
def list_hosts(request):
    hosts = Hosts.objects.order_by('-hostname')
    context = {
        'hosts': hosts
    }
    return render(request, 'inventory/hosts/list_hosts.html', context)


class add_hosts_form(forms.ModelForm):
    class Meta:
        model = Hosts
        fields = '__all__'


@database_error_decorator
@login_required(login_url='/login/')
def add_hosts(request):
    if request.method == 'POST':
        form = add_hosts_form(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            context = {
                'add_success': True,
                'form': form,
            }
            return render(request, 'inventory/hosts/add_hosts.html', context)
        else:
            context = {
                'form_error': False,
                'add_success': False,
                'form': form,
            }
            return render(request, 'inventory/hosts/add_hosts.html', context)
    if request.method == 'GET':
        form = add_hosts_form()
        context = {
            'form': form
        }
        return render(request, 'inventory/hosts/add_hosts.html', context)


@database_error_decorator
@login_required(login_url='/login/')
def modify_hosts(request):
    fields = Hosts.objects.all().values()

    if request.method == 'POST':
        if request.POST.get('hostname') != '' and request.POST.get('old_hostname') != request.POST.get(
                'hostname'):
            context = {
                'form_error': True,
                'fields': fields,
            }
            return render(request, 'inventory/hosts/modify_hosts.html', context)
        elif request.POST.get('action') == 'modify':
            # How to change a django QueryDict to Python Dict?
            # http://stackoverflow.com/questions/13349573/how-to-change-a-django-querydict-to-python-dict
            form_dict = request.POST.dict()  # myDict = dict(queryDict.iterlists())
            form_dict_key_list = form_dict.keys()
            for key in form_dict_key_list:
                if form_dict[key] == '' or key in ['old_hostname', 'action', 'csrfmiddlewaretoken']:
                    del form_dict[key]
                else:
                    if form_dict[key].isdigit():
                        form_dict[key] = int(form_dict[key])
            if len(form_dict.keys()) != 0:
                # update fields
                obj = Hosts.objects.get(hostname=request.POST.get('old_hostname'))
                for key, value in form_dict.items():
                    setattr(obj, key, value)
                obj.save()

                # # update fields using update_or_create()
                # Hosts.objects.update_or_create(
                #     hostname=request.POST.get('old_hostname'), defaults=form_dict
                # )

                context = {
                    'form_error': False,
                    'form_ismodified': True,
                    'fields': fields,
                }
                return render(request, 'inventory/hosts/modify_hosts.html', context)
            else:
                context = {
                    'form_error': False,
                    'form_ismodified': False,
                    'fields': fields,
                }
                return render(request, 'inventory/hosts/modify_hosts.html', context)
        elif request.POST.get('action') == 'delete':
            obj = Hosts.objects.get(hostname=request.POST.get('hostname_to_delete'))
            obj.delete()
            context = {
                'form_error': False,
                'form_isdeleted': True,
                'fields': fields,
            }
            return render(request, 'inventory/hosts/modify_hosts.html', context)
    elif request.method == 'GET':
        context = {
            'form_error': False,
            'fields': fields,
        }
        return render(request, 'inventory/hosts/modify_hosts.html', context)

    else:
        return redirect('/modify_hosts/')
