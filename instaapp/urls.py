from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('profile', views.profile, name='profile'),
    path('post/', views.post, name='post'),
    path('comment/<id>', views.comment, name='comment'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('acounts/profile/', views.profile, name='profile')
    ]