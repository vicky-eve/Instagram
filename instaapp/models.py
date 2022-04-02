from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField('Caption(optional)',max_length=300, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

class Profile(models.Model):
    bio = models.TextField(max_length=500, default='Bio', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='images/')

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, user):
        return cls.objects.filter(user__username__icontains=user).all()

    def __str__(self):
        return f'{self.user.username}'
