from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from hb.user_server import get_status, add_to_queue 
from .forms import QueueForm

def form(request):
    isValidInput = True
    
    if request.method == 'POST':
        form = QueueForm(request.POST)
        if form.is_valid():
            # get user input
            u = request.POST.get('username', None)
            e = request.POST.get('email', None)
            p = request.POST.get('password', None)
            # add this user to queue
            feedback = add_to_queue(u,e) 
            if feedback["error"]: isValidInput = False
            else: # redirect to status page 
                return HttpResponseRedirect(reverse('queue:status', args=(u,)))
        else: isValidInput = False
    else:
        form = QueueForm() 
    return render(request, 'queue/form.html', 
                      {'validInput': isValidInput, 'form':form})

# garuntee to have a valide status?
def status(request, username): 
    try:
        status = get_status(username)
    except TimeOut:
        return HttpResponse("server timeout")
    print(status)
    if status["error"]: return HttpResponse("sorry you haven't sign up yet")
    if status["banned"]: # double check: is this a boolean?
        return render(request, 'queue/banned.html')
    else:
        return render(request, 'queue/status.html',
            {'username':username, 
             'queue_position':status["queue_position"],
             'off_queue':status["off_queue"]})

def index(request):
    return render(request, 'queue/index.html')
