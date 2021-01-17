from django.db import models


# Create your models here.
class VideoItem(models.Model):
    CAT_CHOICES = (
        (0, 'Música'),
        (1, 'Cine'),
        (2, 'Animales'),
        (3, 'Ciencia'),
        (4, 'Otros')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()

    category = models.IntegerField(
        choices=CAT_CHOICES,
        default=0
    )
    image_preview = models.ImageField(upload_to='video_collection/uploaded', default="")
    youtube_id = models.CharField(max_length=100)
