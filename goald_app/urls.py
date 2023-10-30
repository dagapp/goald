from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login",    views.login,    name="login"),
    path("register", views.register, name="register"),

    path("create", views.create, name="create"),
    path("auth",   views.auth,   name="auth"),
    path("deauth", views.deauth, name="deauth"),
    path("change", views.change, name="change"),
    path("delete", views.delete, name="delete"),

    path("users",  views.users,  name="users"),
    path("duties", views.duties, name="duties"),
    path("goals",  views.goals,  name="goals"),

    path("create_group", views.create_group, name="create_group"),

    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('upload_group_image/<int:group_id>/', views.upload_group_image, name='upload_group_image'),
    path('groups/<int:group_id>/user_adding/', views.user_adding, name='user_adding'),
    path('groups/<int:group_id>/goal_create/', views.goal_create, name='goal_create'),

    path("home", views.home, name="home"),
]


