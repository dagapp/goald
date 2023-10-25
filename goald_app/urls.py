from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login, name="login"),
    path("register", views.register, name="register"),

    path("auth", views.auth, name="auth"),
    path("create", views.create, name="create"),

    path("change", views.change, name="change"),
    path("delete", views.delete, name="delete"),

    path("users", views.users, name="users"),
    path("duties", views.duties, name="duties"),

    path("home", views.home, name="home"),
]


