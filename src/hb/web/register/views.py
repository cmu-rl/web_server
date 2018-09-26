from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from hb.user_server import add_user
from .forms import SignupForm
import sys

####### helper function ####### 
# assume form.is_valid is false
def getErrMsg(form):
    # update msg here, assume only one error
    error = form.errors.as_data()
    for k,v in error.items():
        msg = str(v[0])[2:-2] # hardcoded formatting
    return msg

def getUserInput(request):
    u = request.POST.get('username', None)
    e = request.POST.get('email', None)
    p = request.POST.get('password', None)
    r = request.POST.get('repwd', None)
    return (u,e,p,r)

####### views ####### 
def index(request):
    return render(request, "register/index.html")


def form(request):
    # initialization
    valid = True
    msg = ""

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # add new user
            (u,e,p,r) = getUserInput(request)
            try:
                feedback = add_user(u, e, p)
            except Exception as e:
                print(e)
                return HttpResponse("Error:%s" % e)
            if not feedback['error']: # sucess and redirect
                return HttpResponseRedirect(reverse('login:status', 
                                                     args=(u,)))
            else:  # stay on the page
                valid = False
                msg = feedback['message']

        else:
            valid = False
            msg = getErrMsg(form)
            
    else:
        form = SignupForm()
    return render(request, "register/form.html",
        {'valid': valid, 'msg':msg, 'form':form})
