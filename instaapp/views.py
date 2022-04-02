from django.shortcuts import render
from .forms import NewsletterForm, SignupForm

# Create your views here.
def sign_up(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form=SignupForm()
        return render (request, 'signup.html', {"form":form})

def news(request):
    if request.method=='POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form=NewsletterForm()
        return render (request, 'news.html', {"form":form})
