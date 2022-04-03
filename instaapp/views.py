from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewsLetterForm, SignupForm
from .models import NewsLetterRecipients
from .email import send_welcome_email
from django.contrib import messages

# Create your views here.
def news_today(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_Today')
    else:
        form = NewsLetterForm()
    return render(request, 'news.html', {"letterForm":form})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} you have successfully created your account')
            return redirect ('login')
    else:
        form=SignupForm()
        return render (request, 'signup.html', {"form":form})


