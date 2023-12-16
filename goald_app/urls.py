'''
File for defining url paths and corresponding handlers in Django notation
'''

from django.urls import path

from goald_app import views

urlpatterns = [
    path("", views.index, name="index"),

    path("home", views.home, name="home"),

    path("login",    views.login,    name="login"),
    path("register", views.register, name="register"),

    path("user/create", views.user_create, name="user/create"),
    path("user/auth",   views.user_auth,   name="user/auth"  ),
    path("user/deauth", views.user_deauth, name="user/deauth"),
    path("user/change", views.user_change, name="user/change"),
    path("user/delete", views.user_delete, name="user/delete"),

    path("test/users",  views.test_users,  name="test/users" ),
    path("test/duties", views.test_duties, name="test/duties"),
    path("test/goals",  views.test_goals,  name="test/goals" ),

    path("group/create",                      views.group_create,       name="group/create"      ),
    path("group/<int:group_id>",              views.group,              name="group"             ),
    path("group/<int:group_id>/image/update", views.group_image_update, name="group/image/update"),
    path("group/<int:group_id>/users/add",    views.group_user_add,     name="group/users/add"   ),
    path("group/<int:group_id>/goals/add",    views.group_goal_add,     name="group/goals/add"   ),
]
