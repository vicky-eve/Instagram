from email.mime import image
from django import forms
from .models import User, Image, Profile, Comments, Follow
from django.contrib.auth.forms import UserCreationForm
from emoji_picker.widgets import EmojiPickerTextareaAdmin


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    
    
    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']
        help_texts = {'username':None, 'password2':None}
User._meta.get_field('email')._unique = True

class NewsLetterForm(forms.Form):
    username = forms.CharField(label='User_ame',max_length=30)
    email = forms.EmailField(label='Email')

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'caption']

class UpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'email')

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=EmojiPickerTextareaAdmin)
    class Meta:
        model = Comments
        fields = ('comment',)
   
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('photo','bio')