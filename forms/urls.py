from django.urls import path

from . import views

urlpatterns = [
    # path("", FormView.render(FormView)),
    path("", views.index, name="index"),
]
