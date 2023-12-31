"""
File for defining url paths and corresponding handlers in Django notation
"""

from django.urls import path

from goald_app import views


urlpatterns = [
    path("", views.common.home, name="home"),

    # auth handlers
    path("login",    views.common.login,    name="login"),
    path("register", views.common.register, name="register"),
    path("logout",   views.common.logout,   name="logout"),

    # user handlers
    path("user/summary", views.user.user.summary, name="user/summary"),

    path("user/change",  views.user.user.change,  name="user/change" ),
    path("user/delete",  views.user.user.delete,  name="user/delete" ),

    # group handlers
    path("group/<int:group_id>",              views.group.group.view,   name="group"             ),
    path("group/list",                        views.group.group.list,   name="group/list"        ),

    path("group/create",                      views.group.group.create, name="group/create"      ),
    path("group/<int:group_id>/image/update", views.group.image.update, name="group/image/update"),
    path("group/users/add",    views.group.user.add,     name="group/users/add"   ),
    path("group/<int:group_id>/goals/add",    views.group.goal.add,     name="group/goals/add"   ),

    # report handlers
    path(
        "group/<int:goal_id>/reports/create",
        views.report.report.create,
        name="group/report/create"
    ),

    path(
        "report/<int:report_id>",
        views.report.report.view,
        name="report"
    ),
    path(
        "report/<int:report_id>/proof/update",
        views.report.proof.update,
        name="report/proof/update"
    ),
    path(
        "report/<int:report_id>/text/update",
        views.report.text.update,
        name="report/text/update"
    ),

    # duty handlers
    path("goal/duty/pay",      views.duty.duty.pay,         name="goal/duty/pay"     ),
    path("goal/duty/delegate", views.duty.duty.delegate,    name="goal/duty/delegate"),
]
