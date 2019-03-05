from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index/', views.index, name='index'),
    path('getname/', views.get_name, name = 'get_name'),
    path('login/', views.homepage, name='login'),
]