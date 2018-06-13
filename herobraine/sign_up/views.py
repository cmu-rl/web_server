from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
#from .forms import UserForm
from .server import add_user, get_status

def form(request):
    if request.method == 'POST':
        # send username and email to user server
        u = request.POST.get('username', None)
        p = request.POST.get('email', None)
        feedback = add_user(u,p)
        if feedback["status"] == "valid":
            return HttpResponseRedirect(reverse('sign_up:status', args=(u,)))
        else:
            return render(request, 'sign_up/form.html', {'validInput': False})
    else:
        #form = UserForm
        #return render(request, 'sign_up/form.html', {'form': form})
        return render(request, 'sign_up/form.html', {'validInput': True})

def status(request, username): 
    status = get_status(username)
    if status["banned"]: # double check: is this a boolean?
        return render(request, 'sign_up/banned.html')
    else:  
        return render(request, 'sign_up/status.html',
            {'username':username, 'queue_position':status["queue_position"]})

def index(request):
    return render(request, 'sign_up/index.html')

