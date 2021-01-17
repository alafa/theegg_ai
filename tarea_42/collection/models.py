from django.db import models


# Create your models here.
class VideoItem(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.IntegerField(
        choices=(
            (0, 'Música'),
            (1, 'Cine'),
            (2, 'Animales'),
            (3, 'Ciencia'),
            (4, 'Otros')
        ),
        default=0
    )
    image_preview = models.ImageField(upload_to='video_collection/uploaded', default="")
    url = models.CharField(max_length=100)
