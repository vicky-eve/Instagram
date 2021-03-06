from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('images')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField('Caption(optional)',max_length=300, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.user.username}Image'

    class Meta:
        ordering = ['-date_posted']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete

    

class Profile(models.Model):
    bio = models.TextField(max_length=500, default='Bio', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='images/')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

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

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower}Follow'

class Comments(models.Model):
    comment = models.TextField(max_length = 500)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    date_comment_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_comment_posted"]

    def __str__(self):
        return f'{self.image.name}Image'

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Like(models.Model):
    image=models.ForeignKey(Image,on_delete=models.CASCADE, related_name='upvotes')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def str(self):
        return self.image
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['user', 'image'] , name="unique_like"),
        ]
