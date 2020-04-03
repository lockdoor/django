from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home),
    path('home', views.home),    
    path('writeBlogForm', views.writeBlogForm),
    path('addblog', views.addblog),
    path('newMemberForm', views.newMemberForm),
    path('addNewMember', views.addNewMember),
    path('loginForm', views.loginForm),
]