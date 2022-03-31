from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def sign_up(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form=SignupForm()
        return render (request, 'signup.html', {"form":form})
