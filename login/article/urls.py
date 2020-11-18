from django.urls import path

from article import views

urlpatterns = [
    path('typeinit/',views.typeinit),
    path('articleadd/',views.articleadd),
    path('articlelist/',views.articlelist),
]