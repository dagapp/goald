"""
File for defining middleware classes
"""

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from .models import User


class AuthorizationMiddleware:
    '''
    Authorization middleware
    all authorization should be here
    '''

    def __init__(self, get_response):
        """
        One-time configuration and initialization.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request
        """

        if not request.session.has_key("id"):
            if request.path not in ["/login", "/register"]:
                response = Response(
                    data={"detail": "You are not authenticated"},
                    headers={"Location": "/login"},
                    status=status.HTTP_302_FOUND
                )
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response

            return self.get_response(request)

        if not User.objects.filter(id=request.session["id"]).exists():
            response = Response(
                data={"detail": "You are not authenticated"},
                headers={"Location": "/login"},
                status=status.HTTP_302_FOUND
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response

        return self.get_response(request)
