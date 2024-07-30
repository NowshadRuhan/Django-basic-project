import os
from django.conf import settings
from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible

@deconstructible
class DefaultImageStorage(FileSystemStorage):
    def _save(self, name, content):
        if content.size == 0:
            # Use default image if no image is provided
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'default_musician.jpg')
            with open(default_image_path, 'rb') as f:
                content = ContentFile(f.read())
        return super()._save(name, content)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    image = models.ImageField(upload_to='musicians/', storage=DefaultImageStorage(), blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.instrument}"

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent!"),
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return f"{self.name}, Rating: {self.num_stars}"
