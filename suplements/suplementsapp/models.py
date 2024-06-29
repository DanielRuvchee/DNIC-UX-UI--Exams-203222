from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Suplement(models.Model):
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    code = models.IntegerField()
    manufactor = models.CharField(max_length=100)
    is_available = models.BooleanField(default=False)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suplements')

    def __str__(self):
        return self.name
    


class UploadImage(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
