from django.shortcuts import render
from django.http import HttpResponse

def adminDashboard(request):
    return HttpResponse("you're at the administration dashboard :)")
    #return render(request, 'login.html')
