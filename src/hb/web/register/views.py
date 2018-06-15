from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .user_server_helper import add_user

def index(request):
    return render(request, "register/index.html")

def form(request):
    if request.method == 'POST':
        u = request.POST.get('username', None)
        e = request.POST.get('email', None)
        add_user(u, e)
        page =  HttpResponseRedirect(reverse('queue:status', args=(u,)))
        return page
    else:
         return render(request, "register/form.html")
