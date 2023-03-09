from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
     path("Guine", views.Guine, name="Guine"),
    path("Senegal", views.Senegal, name="Senegal")
]