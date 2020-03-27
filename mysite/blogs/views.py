from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    datas = Post.objects.all()
    return render(request, "index.html", {'datas':datas})

def writeblog(request):
    return render(request, "writeblog.html")

def addblog(request):
    
    name = request.POST['name']
    description = request.POST['description']
    
    obj = {
        'name' : name,
        'description' : description
    }
    return render(request, "result.html", obj)
    
    