from django.urls import path
from . import views

urlpatterns = [
    # path("welcome", views.welcome),
    # path("about", views.about),
    path("", views.empty),
    path("<int:input>", views.id_index),
    path("<str:input>", views.index, name="index"),
]
