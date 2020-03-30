from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    datas = Post.objects.all()
    return render(request, "index.html", {'datas':datas})

def writeBlogForm(request):
    return render(request, "writeBlogFrom.html")

def addblog(request):
    name = request.POST['name']
    desc = request.POST['description']
    blog = Post(name = name, desc = desc)
    blog.save()
    return render(request, "result.html", {'message':'success'})
    
def newMemberForm(request):
    return render(request, 'newMemberForm.html')

def addNewMember(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    message = ''
    if not username or not email or not password or not repassword:
        message = 'กรุณากรอกข้อมูลให้ครบ'           
    else:
        if password != repassword:
            message = 'password ไม่ตรงกัน'
        else:
            user = User(username=username,email=email,password=password)
            user.save()
            message = 'success'
    return render(request, 'newMemberForm.html', {'message':message})  

def loginForm(request):
    return render(request, 'loginForm.html')

def login(request):
    return render(request, 'result.html')