from django.shortcuts import render
from django.http import HttpResponse

def adminDashboard(request):
    return HttpResponse("you're at the admin dashboard :)")
    #return render(request, 'login.html')
