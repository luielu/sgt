from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("India", views.India, name="India"),
    path("Japão", views.Japão, name="Japão"),
    path("Coreiadosul", views.Coreiadosul, name="Coreiadosul")
]
