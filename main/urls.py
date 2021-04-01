from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("organisations", views.organisations, name="organisations"),
    path("signUp", views.signUp, name="signUp"),
    path("aboutUs", views.aboutUs, name="aboutUs")
]