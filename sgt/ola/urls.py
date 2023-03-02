from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="dois"),
    # path("<str:nome>", views.saudacao, name="saudacao"),
    # path("Francinaldo", views.greet, name="greet")
    # path("<str:nome>", views.greet, name="greet"),
    path("<str:nome>", views.tia, name="tia")
]
