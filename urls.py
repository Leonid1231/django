from django.urls import path
from . import views
urlpatterns = [
    path("", views.home),
    path("greeting/", views.greeting),
    path("introduction/", views.introduction),
    path("current_time/", views.current_time),
    path("dict_/", views.dict_)
]