from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from hb.user_server import add_user
from .forms import SignupForm

def index(request):
    return render(request, "register/index.html")

def form(request):
    isValidInput = True
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # get user input
            u = request.POST.get('username', None)
            e = request.POST.get('email', None)
            p = request.POST.get('password', None)
            r = request.POST.get('repwd', None)
            print("try to add new user: ", u)
            # add new user
            feedback = add_user(u, e)
            if feedback["error"]: 
                isValidInput = False # and stay on the page
                print("failed to add user ", u)
            else: # sucess and redirect
                return HttpResponseRedirect(reverse('queue:status', args=(u,)))
        else:
            print("django thinks it is bad")
            print("reason:", form.errors)
            isValidInput = False
    else:
        form = SignupForm()
    return render(request, "register/form.html",
        {'validInput': isValidInput, 'form':form})
