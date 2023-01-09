from django.urls import path, include
from articles import views

urlpatterns = [
    path("index/", views.index, name="index"),
]