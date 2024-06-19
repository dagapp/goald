"""
File for defining handlers for Image in Django notation
"""

from rest_framework import mixins, viewsets

from ..models import Image
from ..serializers import ImageSerializer
from ..paginations import ImageViewSetPagination
from ..permissions import ImagePermission


class ImageViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    ViewSet for an image model
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [ImagePermission]
    pagination_class = ImageViewSetPagination
