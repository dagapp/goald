"""
File for defining url paths and corresponding handlers in Django notation
"""

from django.urls import include, path

from rest_framework import routers

from goald_app import views


router = routers.DefaultRouter()
router.register("auth",   views.auth.AuthViewSet,     basename="auth"  )
router.register("group",  views.group.GroupViewSet,   basename="group" )
router.register("goal",   views.goal.GoalViewSet,     basename="goal"  )
router.register("duty",   views.duty.DutyViewSet,     basename="duty"  )
router.register("report", views.report.ReportViewSet, basename="report")
router.register("events", views.event.EventViewSet,   basename="events")
router.register("image",  views.image.ImageViewSet,   basename="image" )

urlpatterns = [
    path("", include(router.urls))
]
