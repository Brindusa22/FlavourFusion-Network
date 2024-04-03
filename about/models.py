from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__ (self):
        return f"{self.name} | last updated on  {self.date_updated}"
