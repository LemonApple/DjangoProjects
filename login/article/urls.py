from django.urls import path

from article import views

urlpatterns = [
    path('articlelist/',views.articlelist),
]