"""
File for defining url paths and corresponding handlers in Django notation
"""

from django.urls import include, path

from rest_framework import routers

from goald_app import views


router = routers.DefaultRouter()
router.register("group",  views.group.GroupViewSet,   basename="group" )
router.register("goal",   views.goal.GoalViewSet,     basename="goal"  )
router.register("duty",   views.duty.DutyViewSet,     basename="duty"  )
router.register("report", views.report.ReportViewSet, basename="report")

urlpatterns = [
    path("register/", views.auth.register, name="register"),
    path("login/",    views.auth.login,    name="login"   ),
    path("logout/",   views.auth.logout,   name="logout"  ),
    path("", include(router.urls)),
    path("events/",   views.event.EventView.as_view(), name="events")
]
