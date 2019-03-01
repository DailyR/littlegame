
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path(r'show_data', views.show_data, name='show_data'),
    path(r'create_data', views.create_data, name='create_data'),
]