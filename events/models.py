from django.db import models


class Event(models.Model):
    event_image = models.ImageField(upload_to='media/event_images/')
    event_text = models.CharField(max_length=300)

    event_manager = models.Manager()

