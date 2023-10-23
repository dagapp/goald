from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login, name="login"),
    path("register", views.register, name="register"),

    path("auth", views.auth, name="auth"),
    path("create", views.create, name="create"),

    path("users", views.users, name="users"),

    path("home", views.home, name="home"),
]


