from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

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
    """
    Stores a recipe entry related to  :model: `auth.User`.
    """
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
    recipe_image = CloudinaryField('image', default="placeholder")
    meal_type = models.CharField(max_length=30, choices = MEAL_TYPE)
    cuisine = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add=True)
    status =  models.IntegerField(choices=STATUS, default=0)

    # Code to generate a unique slug combining title and username inspired from:
    #  https://www.kodnito.com/posts/slugify-urls-django/
    def save(self, *args, **kwargs):
        """
        Override the save method to generate a unique slug if it doesn't exist.
        """
        if not self.slug:
            slug = slugify(self.title)
            unique_slug = f"{slug}-{self.author.username}"
            self.slug = unique_slug
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Recipe by {self.author}"


class RecipeRating(models.Model):
    """
    Stores information about a specific review given by a user for a particular recipe.
    Related to :model: `Recipe` and `auth.User'

    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Rating for {self.recipe.title} | {self.comment} by {self.author}"


class UserProfile(models.Model):
    """
    Stores additional information(user image) about a user.
    Related to :model:`auth.User`.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    user_image = CloudinaryField('image', default="placeholder")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", null=True)

    def __str__(self):
        return self.user.username  