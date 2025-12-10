from django.urls import path
from . import views

urlpatterns = [
    path("work05/", views.work05_index, name="index"),
    path("work06/", views.work06_index, name="index"),
    path("work07/", views.work07_index, name="index"),
    path("facebank/", views.facebank_index, name="index"),
    path("", views.top_index, name="top_index"),
]
