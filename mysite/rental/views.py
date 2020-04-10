from django.shortcuts import render
#from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    obj = {
        'text': 'This is index of Rental app',
        'admin' : False
    }
    if not obj['admin']:        
        return render(request, 'rental/loginForm.html')
    else:
        return render(request, 'rental/index.html', obj)

def login(request):
    if request.POST['username'] and request.POST['password']:
        return render(request, 'rental/index.html',{'username':request.POST['username']})
    else:
        return render(request, 'rental/loginForm.html', {
            'error_message': "please insert username and password"
        })

    