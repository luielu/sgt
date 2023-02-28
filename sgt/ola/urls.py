from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dois"),
    path("<str:nome>", views.saudacao, name="saudacao")
]
