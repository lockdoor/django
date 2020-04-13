from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    obj = {
        'text': 'This is index of Rental app',
        'admin' : False
    }
    if not obj['admin']:        
        return HttpResponseRedirect('loginForm')
    else:
        return render(request, 'rental/index.html', obj)

def loginForm(request):
    return render(request, 'rental/loginForm.html')

def login(request):
    if request.POST['username'] and request.POST['password']:
        return render(request, 'rental/index.html',{'username':request.POST['username']})
    else:
        
        message = {'message': "please insert username and password"}
        
        return HttpResponseRedirect(reverse('rental:loginForm',args=(message,)))

    