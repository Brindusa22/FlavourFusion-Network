from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

MEAL_TYPE = [('breakfast', 'Breakfast'),
            ('appetizer', 'Appetizer'),
            ('main_course', 'Main Course'),
            ('soup', 'Soup'),
            ('sides', 'Sides'),
            ('dessert', 'Dessert'),
        ]

STATUS = [(0, 'Draft'),
         (1, 'Published'),
         (2, 'Flagged for Revision')
        ]

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    total_time = models.CharField(max_length=50)
    servings = models.PositiveIntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    meal_type = models.CharField(max_length=30, choices = MEAL_TYPE)
    cuisine = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add=True)
    status =  models.IntegerField(choices=STATUS, default=0)

    # Code to generate a unique slug combining title and username inspired from https://www.kodnito.com/posts/slugify-urls-django/
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            unique_slug = f"{slug}-{self.author.username}"
            self.slug = unique_slug
        super(Recipe, self).save(*args, **kwargs)