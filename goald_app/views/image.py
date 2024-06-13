"""
File for defining handlers for Image in Django notation
"""

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from ..models import Image
from ..serializers import ImageSerializer
from ..paginations import ImageViewSetPagination
from ..permissions import ImagePermission


class ImageViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    ModelViewSet for a image model
    """

    serializer_class = ImageSerializer
    pagination_class = ImageViewSetPagination
    permission_classes = [ImagePermission]
    queryset = Image.objects.all()
