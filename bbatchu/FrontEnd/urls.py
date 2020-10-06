from django.contrib import admin
# from django.utils import path
# from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('home', views.home, name='home'),
    # url('', views.home, name='home'),
    url('signup', views.signup, name='signup'),
    url('login', views.login, name='login'),
    url('logout', views.logout, name='logout'),
    # url('base', views.base, name='base'),
    url('contact', views.contact, name='contact'),
    url('about', views.about, name='about')
]
