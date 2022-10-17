from django.urls import path

from . import views

urlpatterns = [
    path("", views.FileView.as_view()),
]
