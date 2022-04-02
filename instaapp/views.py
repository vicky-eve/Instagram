from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewsLetterForm, SignupForm

# Create your views here.
def news(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('news')
    else:
        form = NewsLetterForm()
    return render(request, 'news.html', {"date": date,"news":news,"letterForm":form})


def sign_up(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form=SignupForm()
        return render (request, 'signup.html', {"form":form})


