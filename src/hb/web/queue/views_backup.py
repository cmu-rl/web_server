from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .user_server_helper import get_status, add_to_queue

def form(request):
    if request.method == 'POST':
        # Add user to queue
        u = request.POST.get('username', None)
        p = request.POST.get('email', None)
        # add try except here later
        feedback = add_to_queue(u,p) 
        if not feedback["error"]: # valid input
            return HttpResponseRedirect(reverse('queue:status', args=(u,)))
        else: # invalid input
            return render(request, 'queue/form.html', {'validInput': False})
    else:
        return render(request, 'queue/form.html', {'validInput': True})

def status(request, username): 
    try:
        status = get_status(username)
    except TimeOut:
        return HttpResponse("server timeout")
    if status["banned"]: # double check: is this a boolean?
        return render(request, 'queue/banned.html')
    else:
        return render(request, 'queue/status.html',
            {'username':username, 
             'queue_position':status["queue_position"],
             'off_queue':status["off_queue"]})

def index(request):
    return render(request, 'queue/index.html')
