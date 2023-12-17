'''
File for defining url paths and corresponding handlers in Django notation
'''

from django.urls import path

from goald_app import views


urlpatterns = [
    path("", views.common.index, name="index"),

    path("home", views.common.home, name="home"),

    path("login",    views.common.login,    name="login"),
    path("register", views.common.register, name="register"),

    path("user/create", views.user.create, name="user/create"),
    path("user/auth",   views.user.auth,   name="user/auth"  ),
    path("user/deauth", views.user.deauth, name="user/deauth"),
    path("user/change", views.user.change, name="user/change"),
    path("user/delete", views.user.delete, name="user/delete"),

    path("test/users",  views.test.users,  name="test/users" ),
    path("test/duties", views.test.duties, name="test/duties"),
    path("test/goals",  views.test.goals,  name="test/goals" ),

    path("group/create",                      views.group.group.create, name="group/create"      ),
    path("group/<int:group_id>",              views.group.group.view,   name="group"             ),
    path("group/<int:group_id>/image/update", views.group.image.update, name="group/image/update"),
    path("group/<int:group_id>/users/add",    views.group.user.add,     name="group/users/add"   ),
    path("group/<int:group_id>/goals/add",    views.group.goal.add,     name="group/goals/add"   ),
]
