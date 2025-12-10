from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("select/", views.select_mood, name="select_mood"),
    path("result/<str:mood>/<int:amount>/", views.result, name="result"),
    path("history/", views.history, name="history"),
    path("history/reset/", views.reset_history, name="history_reset"),
]
