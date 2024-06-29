from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

