from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    

class Book(models.Model):
    HARDCOVER = 'HC'
    SOFTCOVER = 'SC'

    COVER_CHOICES = [
        (HARDCOVER, 'Hard cover'),
        (SOFTCOVER, 'Soft cover'),
    ]

   
    DRAMA = 'DR'
    ACTION = 'AC'
    THRILER = 'TR'
    ROMANCE = 'RM'
    BIOGRAPHY = 'BI'
    CLASIC = 'CK'

    CATEGORY_CHOICES = [
        (DRAMA, 'Drama'),
        (ACTION, 'Action'),
        (THRILER, 'Thriler'),
        (ROMANCE, 'Romance'),
        (BIOGRAPHY, 'Biography'),
        (CLASIC, 'Clasic'),
     ]

    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default=CLASIC)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    isbn = models.IntegerField()
    year = models.IntegerField()
    publisher = models.CharField(max_length=250)
    num_pages = models.IntegerField()
    dimension = models.CharField(max_length=250)
    cover_type = models.CharField(max_length=2, choices=COVER_CHOICES, default=HARDCOVER)
    price = models.IntegerField()


    def __str__(self):
        return self.title





