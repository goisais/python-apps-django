from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.reiwa_to_seireki, name="index"),
    ]
