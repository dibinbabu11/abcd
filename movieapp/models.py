from distutils.command.upload import upload
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.name
