"""emailAlchemy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from alchemy.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index),
	url(r'^signup/$', signup),
	url(r'^dashboard/$', dashboard),
	url(r'^dashboard/(?P<selecteduemail>[0-9]+)$', showUserSelectedEmails),
	url(r'^read/(?P<reademail>[0-9]+)$', reademail),
	url(r'^addnewemail/$', addNewEmail),
	url(r'^deleteemail/(?P<deluseremail>[0-9]+)$', delUserEmail),
	url(r'^spamalyze/(?P<selecteduemail>[0-9]+)$', spamScore),
	url(r'^whitelist/(?P<whiteemail>[0-9]+)$', whitelist),
	url(r'^blacklist/(?P<blackemail>[0-9]+)$', blacklist),
	url(r'^logout/$', logout_view),
]


