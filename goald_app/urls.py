"""
File for defining url paths and corresponding handlers in Django notation
"""

from django.urls import path

from goald_app import views


urlpatterns = [
    path("", views.common.home, name="home"),

    path("login",    views.common.login,    name="login"),
    path("register", views.common.register, name="register"),
    path("logout",   views.common.logout,   name="logout"),

    path("user/change", views.user.change, name="user/change"),
    path("user/delete", views.user.delete, name="user/delete"),

    path("group/create",                      views.group.group.create, name="group/create"      ),
    path("group/<int:group_id>",              views.group.group.view,   name="group"             ),
    path("group/<int:group_id>/image/update", views.group.image.update, name="group/image/update"),
    path("group/<int:group_id>/users/add",    views.group.user.add,     name="group/users/add"   ),
    path("group/<int:group_id>/goals/add",    views.group.goal.add,     name="group/goals/add"   ),

    path(
        "group/<int:goal_id>/reports/create", 
        views.report.report.create, 
        name="group/report/create"
    ), #fixme

    path(
        "report/<int:report_id>",                
        views.report.report.view,        
        name="report"
    ),
    path(
        "report/<int:report_id>/proof/update", 
        views.report.proof.update_proof, 
        name="report/proof/update"
    ),
    path(
        "report/<int:report_id>/text/update",  
        views.report.text.update_text,   
        name="report/text/update"
    ),
]
