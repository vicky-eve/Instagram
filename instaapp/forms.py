from django import forms

class NewsletterForm(forms.Form):
    username = forms.CharField(label='User_ame',max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.PasswordInput(label='Password')