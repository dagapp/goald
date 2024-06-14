"""
File for defining url paths and corresponding handlers in Django notation
"""

from django.urls import include, path

from rest_framework import routers

from backend import views


router = routers.DefaultRouter()
router.register(r"auth",   views.auth.AuthViewSet,     basename="auth"  )
router.register(r"user",   views.user.UserViewSet,     basename="user"  )
router.register(r"group",  views.group.GroupViewSet,   basename="group" )
router.register(r"goal",   views.goal.GoalViewSet,     basename="goal"  )
router.register(r"duty",   views.duty.DutyViewSet,     basename="duty"  )
router.register(r"report", views.report.ReportViewSet, basename="report")
router.register(r"events", views.event.EventViewSet,   basename="events")
router.register(r"image",  views.image.ImageViewSet,   basename="image" )

urlpatterns = [
    path("api/v1/", include(router.urls))
]
