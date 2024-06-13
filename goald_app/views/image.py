"""
File for defining handlers for Image in Django notation
"""

from rest_framework import viewsets, status
from rest_framework.response import Response

from ..models import Image
from ..serializers import ImageSerializer
from ..paginations import ImageViewSetPagination
from ..permissions import ImagePermission


class ImageViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for a image model
    """
    serializer_class = ImageSerializer
    pagination_class = ImageViewSetPagination
    permission_classes = [ImagePermission]
    queryset = Image.objects.all()

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN) 

    def retrieve(self, request, *args, **kwargs):
        try:
            image = self.get_object()
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ImageSerializer(image)
        return Response(serializer.data)
