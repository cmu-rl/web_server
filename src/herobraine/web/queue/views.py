from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
#from .forms import UserForm
from ..server import add_user, get_status, add_to_queue

def form(request):
    if request.method == 'POST':
        # send username and email to user server
        u = request.POST.get('username', None)
        p = request.POST.get('email', None)
        # add try to handle exception here
        "sorry our server is down. please try again later"
        feedback = add_to_queu(u,p) # should be add_to_queue
        if feedback["status"] != "valid": # buggy here
            return HttpResponseRedirect(reverse('queue:status', args=(u,)))
        else:
            return render(request, 'queue/form.html', {'validInput': False})
    else:
        return render(request, 'queue/form.html', {'validInput': True})

def status(request, username): 
    try:
        status = get_status(username)
    except:
        return HttpResponse("server timeout")
    if status["banned"]: # double check: is this a boolean?
        return render(request, 'queue/banned.html')
    else:  
        return render(request, 'queue/status.html',
            {'username':username, 'queue_position':status["queue_position"]})

def index(request):
    return render(request, 'queue/index.html')

