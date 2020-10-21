from django.urls import path
from . import views

urlpatterns = [
    path("", views.newsIndex, name="newsIndex"),
    path("newsScore/", views.newsScore, name="newsScore"),
    path("about/", views.about, name="about"),
    path("comments/", views.comments, name="comments"),

]