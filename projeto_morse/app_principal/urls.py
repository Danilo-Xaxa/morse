from django.urls import path
from . import views

urlpatterns = [
    path("", views.morse_para_texto, name="morse_para_texto"),
    path("inverso/", views.texto_para_morse, name="texto_para_morse")
]
