from django.shortcuts import render
from django.http import HttpResponse
from django.http import *
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login(request):
    #return HttpResponse("you're at the login page :)")
    return render(request, 'login.html')

def forgotpassword(request):
    #return HttpResponse("you forgot your password :(")
    return render(request, 'forgotpassword.html')

def loginpage(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

