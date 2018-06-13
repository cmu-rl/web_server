from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
#from .forms import UserForm
from .server import add_user, get_status

def form(request):
    if request.method == 'POST':
        # send this user name and password to user server
        u = request.POST.get('username', None)
        p = request.POST.get('email', None)
        #print("username is:", u)
        add_user(u,p)
        return HttpResponseRedirect(reverse('sign_up:status', args=(u,)))
    else:
        #form = UserForm
        #return render(request, 'sign_up/form.html', {'form': form})
        return render(request, 'sign_up/form.html')

def status(request, username): 
    status = get_status(username)
    if status["banned"]:
        return render(request, 'sign_up/banned.html')
    else:  
        return render(request, 'sign_up/status.html',
            {'username':username, 'queue_position':status["queue_position"]})

def index(request):
    return render(request, 'sign_up/index.html')

