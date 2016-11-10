"""kissops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from kissops import views
from login.views import index, login, logout, register, profile
from inventory.host.views import list_hosts, add_hosts, modify_hosts

from django.views.generic.base import RedirectView
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^favicon.ico$', RedirectView.as_view(url=getattr(settings, 'FAVICON_PATH'))),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^list_hosts/$', list_hosts, name='list_hosts'),
    url(r'^add_hosts/$', add_hosts, name='add_hosts'),
    url(r'^modify_hosts/$', modify_hosts, name='modify_hosts'),
]
