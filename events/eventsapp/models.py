from django.db import models
from django.contrib.auth.models import User


class Bands(models.Model):
     name = models.CharField(max_length=244)
     country =  models.CharField(max_length=244)
     year = models.IntegerField()
     performances = models.IntegerField()

     def __str__(self):
        return self.name



class Events(models.Model):
    name = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='event_images', blank=True, null=True)
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    bands = models.ManyToManyField(Bands)
    info = models.BooleanField(default=False)

    def __str__(self):
        return self.name

