from django.conf.urls import patterns, include, url
from django.contrib.auth.views import (
	login as django_login,
    logout as django_logout,
    password_reset as django_password_reset,
    password_reset_done as django_password_reset_done,)

urlpatterns = patterns('',
    url(r'^login/', django_login, {
    	'template_name': 'users/login.html'
    	},
    	name='login'
    ),
)
