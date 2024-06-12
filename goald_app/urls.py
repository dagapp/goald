"""
File for defining url paths and corresponding handlers in Django notation
"""

from django.urls import include, path

from rest_framework import routers

from goald_app import views


router = routers.DefaultRouter()
router.register("group", views.group.GroupViewSet, basename="group")
router.register("goal",  views.goal.GoalViewSet,   basename="goal" )
router.register("duty",  views.duty.DutyViewSet,   basename="duty" )


urlpatterns = [
    path("api/v1/", include([
        path("register/", views.auth.register, name="register"),
        path("login/",    views.auth.login,    name="login"   ),
        path("logout/",   views.auth.logout,   name="logout"  ),
    ])),
    path("api/v1/", include(router.urls))
]
