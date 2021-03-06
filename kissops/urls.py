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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from inventory.host.views import list_hosts, add_hosts, modify_hosts
from itoms.views import post, test_json, itoms_app, django_admin, app2question
from kissops import views
from login.views import login, logout, register, profile, management, reset_password, forget_password

admin.autodiscover()

urlpatterns = [
                  url(r'^favicon.ico$', RedirectView.as_view(url=getattr(settings, 'FAVICON_PATH'))),
                  url(r'^robots.txt$', RedirectView.as_view(url=getattr(settings, 'ROBOTS_PATH'))),
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include('api.urls')),
                  url(r'^management$', management, name='management'),
                  url(r'^$', views.index, name='index'),
                  url(r'^login/$', login, name='login'),
                  url(r'^logout/$', logout, name='logout'),
                  url(r'^register/$', register, name='register'),
                  url(r'^profile/$', profile, name='profile'),
                  url(r'^forget_password/$', forget_password, name='forget_password'),
                  url(r'^reset_password/$', reset_password, name='reset_password'),
                  url(r'^list_hosts/$', list_hosts, name='list_hosts'),
                  url(r'^add_hosts/$', add_hosts, name='add_hosts'),
                  url(r'^modify_hosts/$', modify_hosts, name='modify_hosts'),
                  url(r'^post/$', post, name='post'),
                  url(r'^json/$', test_json, name='test_json'),
                  url(r'^itoms_app/$', itoms_app, name='itoms_app'),
                  url(r'^django_admin/$', django_admin, name='django_admin'),
                  url(r'^app2question/$', app2question, name='app2question'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
