from django.db import models
from django.utils.timezone import now


class Video(models.Model):
    title=models.CharField(max_length=50)
    video = models.FileField(upload_to="videos")
    length = models.IntegerField()
    type = models.CharField(max_length=20)
    size = models.IntegerField()
    created_at=models.DateTimeField(default=now)

