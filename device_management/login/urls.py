from django.conf.urls import url
from django.contrib import admin
from login import views

 

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^webye/', views.webye),
    url(r'^contact', views.contact),
    url(r'^', views.index),
]



