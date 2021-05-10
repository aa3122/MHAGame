from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    #return HttpResponse("you're at the login page :)")
    return render(request, 'login.html')

def forgotpassword(request):
    #return HttpResponse("you forgot your password :(")
    return render(request, 'forgotpassword.html')


