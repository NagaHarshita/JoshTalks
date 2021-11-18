from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    channel_id = models.CharField(max_length=30)
    channel_title = models.CharField(max_length=30)
    published_time = models.DateTimeField()
