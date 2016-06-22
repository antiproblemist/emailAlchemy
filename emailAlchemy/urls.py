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
	url(r'^$', 'alchemy.views.index.index'),
	url(r'^signup/$', 'alchemy.views.signup.signup'),
	url(r'^dashboard/$', 'alchemy.views.dashboard.dashboard'),
	url(r'^dashboard/(?P<selecteduemail>[0-9]+)$', 'alchemy.views.showUserSelectedEmails.showUserSelectedEmails'),
	url(r'^read/(?P<reademail>[0-9]+)$', 'alchemy.views.reademail.reademail'),
	url(r'^addnewemail/$', 'alchemy.views.addNewEmail.addNewEmail'),
	url(r'^deleteemail/(?P<deluseremail>[0-9]+)$', 'alchemy.views.delUserEmail.delUserEmail'),
	url(r'^spamalyze/(?P<selecteduemail>[0-9]+)$', 'alchemy.views.spamScore.spamScore'),
	url(r'^whitelist/(?P<whiteemail>[0-9]+)$', 'alchemy.views.whitelist.whitelist'),
	url(r'^blacklist/(?P<blackemail>[0-9]+)$', 'alchemy.views.blacklist.blacklist'),
	url(r'^logout/$', 'alchemy.views.logout.logout_view'),
]


