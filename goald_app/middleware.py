"""
File for defining middleware classes
"""

from django.shortcuts import redirect


class AuthorizationMiddleware:
    """
    Authorization middleware
    all authorization should be here
    """

    def __init__(self, get_response):
        """
        One-time configuration and initialization.
        """
        self.permited_wo_id = ["/login", "/register", "/user/auth", "/user/create"]
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request
        """
        path = request.path
        session = request.session

        if not session.has_key("id"):
            if path in self.permited_wo_id:
                response = self.get_response(request)
                return response

            return redirect("login")

        if path in self.permited_wo_id:
            return redirect("home")

        response = self.get_response(request)
        return response
