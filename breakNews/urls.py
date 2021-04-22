from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index, name="index"),
    path('news/',  views.news, name="news"),
    path('news/add/',  views.addNews, name="add")
]
