'''
Module for handling images
'''

import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from goald_app.managers.common import ManagerResult


class ImageManager:
    '''
    Manager for handling images
    '''

    @staticmethod
    def store(image) -> ManagerResult:
        '''
        Store an image in a filesystem
        '''
        storage_location = os.path.join(
            settings.MEDIA_ROOT, "group", "images"
        )
        fs = FileSystemStorage(location=storage_location)
        fs.save(image.name, image)
        image_path = "group/images/" + image.name

        return ManagerResult(True, "Imaged is stored successfully", image_path)
