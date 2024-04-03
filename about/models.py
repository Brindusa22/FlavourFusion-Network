from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__ (self):
        return f"{self.name} | last updated on  {self.date_updated}"
