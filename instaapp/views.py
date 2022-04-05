from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import CommentForm, NewsLetterForm, SignupForm, UpdateForm, UpdateProfileForm, UploadPhotoForm
from .models import Comments, NewsLetterRecipients, Image, Profile, Like, Comments
from .email import send_welcome_email
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

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

@login_required(login_url='/registration/register/')
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} you have successfully created your account')
            return redirect ('login')
    else:
        form=SignupForm()
        return render (request, 'registration/registration_form.html', {"form":form})

@login_required(login_url='/registration/login/')
def index(request):
    """
    displaying posts
    """
    posts=Image.objects.all()
    comments=Comments.objects.all()
    profiles=Profile.objects.all()

    return render(request, 'index.html', {"posts":posts, "comments":comments, "profiles":profiles})

@login_required(login_url='registration/login/')
def profile(request):
    current_user=(request.user)
    images=Image.objects.filter(profile=current_user.id).all
    profile=Profile.objects.filter(user_id=current_user.id).first()
    return (request, 'registration/profile.html', {'images':images, 'profile':profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    photo=request.user.images.all()
    if request.method=='POST':
        form=UpdateForm(request.POST, instance=request.user.profile)
        form1=UpdateProfileForm(request.POST, request.FILES, insance=request.user.profile)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return HttpResponseRedirect(request.path_info)
        else:
            form=UpdateForm(instance=request.user)
            form1=UpdateProfileForm()
        return render (request, 'registrarion/update_profile.html', {'form':form, 'form1':form1,'photo':photo})

@login_required(login_url='/accounts/login')
def post(request):
    if request.method=='POST':
        form=UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.profile=request.user
            if 'image' in request.FILES:
                image.image=request.FILES['image']
            image.save()
        return redirect('/')
    else:
        form=UploadPhotoForm()
    return render(request, 'post.html', {"form":form, })

@login_required(login_url='/accounts/login/')
def comment(request,id):
    post_comment = Comments.objects.filter(image= id)
    image = Image.objects.filter(id=id).first()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.image = image
            comment.user = current_user
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request,'comment.html',{"form":form,"img":image,"comments":post_comment})

@login_required(login_url='/accounts/login/')
def search(request):
    profile=User.objects.all()
    if 'username' in request.GET and request.GET['username']:
        search_profile=request.GET.get('username')
        profiles=User.objects.filter(username__icontains=search_profile)
        print(profiles)
        return render (request, 'search.html', locals())
    return redirect(index)

@login_required(login_url='/accounts/login/')
def like_image(request, image_id):
    image = get_object_or_404(Image,id = image_id)
    like = Like.objects.filter(image = image ,user = request.user).first()
    if like is None:
        like = Like()
        like.image = image
        like.user = request.user
        like.save()
    else:
        like.delete()
    return redirect('index')
