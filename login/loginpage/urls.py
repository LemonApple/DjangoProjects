from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login),
    path('init/', views.init),
    path('index/', views.index),
    path('exit/', views.exit),
    path('welcome/', views.welcome),
]