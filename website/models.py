from django.db import models

# Create your models here.


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to="gallery")


class Images(models.Model):
    photo = models.ImageField()
    gallery = models.ForeignKey(Gallery)
