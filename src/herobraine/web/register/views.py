from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponse("this is the sign up page for new user")

def form(request):
    if request.method == 'POST':
        u = request.POST.get('username', None)
        try:
            page =  HttpResponseRedirect(reverse('queue:status', args=(u,)))
        except timeout :
            return HttpResponse("Sorry our server is down. Please try again later")
        return page
    else:
         return render(request, "register/form.html")
