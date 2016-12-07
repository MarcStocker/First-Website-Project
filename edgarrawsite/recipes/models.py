from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField(max_length=2000, null=True, blank=True)
    recipe = models.TextField(max_length=2000, null=True, blank=True)
    ingredients = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(max_length=144, upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        Recipe.objects.order_by('-self.id')
        return str(self.id) + " - " + self.title
