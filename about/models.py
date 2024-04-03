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


class RecipePostRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    user_recipe_img = CloudinaryField('image', blank=True, null=True)
    user_recipe_doc = CloudinaryField('document', blank=True, null=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        is_read = "Read" if self.read else "Unread"
        return f"Recipe post request from {self.name} | status : {is_read}"