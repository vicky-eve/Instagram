from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField('Caption(optional)',max_length=300, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

