from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("organisations", views.organisations, name="organisations"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    path("account", views.user, name="user"),
    path("signUp", views.signUp, name="signUp")
]