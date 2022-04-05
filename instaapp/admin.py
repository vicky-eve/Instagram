from django.contrib import admin
from .models import Image, Profile, Comments, Follow, NewsLetterRecipients, Like

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Follow)
admin.site.register(NewsLetterRecipients)
admin.site.register(Like)

