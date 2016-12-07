from django.db import models

# Create your models here.

class edgar(models.Model):
    banner = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(max_length=144, upload_to='websiteimages/%Y/%m/%d/', null=True, blank=True)
    num_followers = models.DecimalField(decimal_places=1, max_digits=4)
    num_posts = models.IntegerField()
    num_following = models.IntegerField()
    insta_url = models.CharField(max_length=144)
    insta_image = models.ImageField(max_length=144, upload_to='websiteimages/%Y/%m/%d/', null=True, blank=True)
    fb_image = models.ImageField(max_length=144, upload_to='websiteimages/%Y/%m/%d/', null=True, blank=True)
    fb_url = models.CharField(max_length=144)
    email = models.CharField(max_length=144)

    def __str__(self):
        return "Website_Info"
