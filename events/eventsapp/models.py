from django.db import models
from django.contrib.auth.models import User


class Bands(models.Model):
     name = models.CharField(max_length=244)
     country =  models.CharField(max_length=244)
     year = models.IntegerField()
     performances = models.IntegerField()

     def __str__(self):
        return self.name



class Event(models.Model):
    name = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='event_images', blank=True, null=True)
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    bands = models.ManyToManyField(Bands)
    info = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BandEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    band = models.ForeignKey(Bands, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name