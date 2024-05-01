"""
File for defining url paths and corresponding handlers in Django notation
"""

from django.urls import path

from goald_app import views


urlpatterns = [
    # image handlers
    #path("image", views.image.image, name="image"),

    # auth handlers
    path("register", views.user.UserView.post, name="register"),
    path("login",    views.user.login,         name="login"   ),
    path("logout",   views.user.logout,        name="logout"  ),

    # user handlers
    path("user/<int:id>", views.user.UserView.as_view(), name="user"),
    path("user",          views.user.UserView.as_view(), name="user"),

    #path("user/<int:id>/goals",  views.user.goals,  name="user/goals" ),
    #path("user/<int:id>/groups", views.user.groups, name="user/groups"),
    #path("user/<int:id>/duties", views.user.duties, name="user/duties"),

    # group handlers
    path("group/<int:id>", views.group.GroupView.as_view(), name="group"),
    path("group",          views.group.GroupView.as_view(), name="group"),

    path("group/<int:id>/events", views.event.EventView.as_view(), name="events"),
    #path("group/<int:id>/users",  views.group.users,  name="group/users" ),
    #path("group/<int:id>/goals",  views.group.goals,  name="group/goals" ),
    #path("group/<int:id>/duties", views.group.duties, name="group/duties"),

    # goal handlers
    path("group/<int:id>/goal/<int:goal_id>", views.goal.GoalView.as_view(), name="goal"),
    path("group/<int:id>/goal",               views.goal.GoalView.as_view(), name="goal"),

    #path("goal/<int:id>", views.goal.GoalView.as_view(), name="goal"),

    #path("goal/<int:id>/users",   views.goal.users,   name="goal/users"  ),
    #path("goal/<int:id>/duites",  views.goal.duties,  name="goal/duties" ),
    #path("goal/<int:id>/reports", views.goal.reports, name="goal/reports"),

    # report handlers
    path("report/<int:id>", views.report.ReportView.as_view(), name="report"),
    path("report",          views.report.ReportView.as_view(), name="report"),

    # duty handlers
    path("duty/<int:id>", views.duty.DutyView.as_view(), name="duty"),
    path("duty",          views.duty.DutyView.as_view(), name="duty"),

    #path("duty/<int:id>/pay",      views.duty.duty.pay,      name="duty/pay"     ),
    #path("duty/<int:id>/delegate", views.duty.duty.delegate, name="duty/delegate"),
]
