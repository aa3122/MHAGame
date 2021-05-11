from django.shortcuts import render
from django.http import HttpResponse

def game(request):
    return HttpResponse("you're at /game :)")
    #return render(request, 'login.html')
