from rest_framework.pagination import PageNumberPagination

class DutyViewSetPagination(PageNumberPagination):
    """
    Pagination class for Duty
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class EventViewPagination(PageNumberPagination):
    """
    Pagination class for Event
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class GoalViewSetPagination(PageNumberPagination):
    """
    Pagination class for Goal
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class GroupViewSetPagination(PageNumberPagination):
    """
    Pagination class for Group
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ReportViewSetPagination(PageNumberPagination):
    """
    Pagination class for Report
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ImageViewSetPagination(PageNumberPagination):
    """
    Pagination class for Image
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
