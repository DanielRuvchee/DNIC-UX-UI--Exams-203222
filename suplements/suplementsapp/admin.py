from django.contrib import admin
from .models import Suplement, Category, UploadImage

# Register your models here.

admin.site.register(Suplement)
admin.site.register(Category)
admin.site.register(UploadImage)