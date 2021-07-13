from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.home, name="home"),
    path("organisations", views.organisations, name="organisations"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    path("account", views.user, name="user"),
    path("signUp", views.signUp, name="signUp"),
    path("orgs", views.orgs, name="orgs"),
    path("org", views.org, name="org")
]