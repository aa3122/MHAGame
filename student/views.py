from django.shortcuts import render
from django.http import HttpResponse

def studentDashboard(request):
    #return HttpResponse("You're at the student dashboard")
    return render(request, 'studentDashboard.html')

def calender(request):
    #return HttpResponse("You're on the Student view of the Calender page")
    return render(request, 'studentCalender.html')

def gameInput(request):
    #return HttpResponse("You're at the student view of the Game Input")
    return render(request, 'studentGameInput.html')

def studentGameOverview(request):
    #return HttpResponse("You're at the student view of the Game Overview")
    return render(request, 'studentGameOverview.html')

def profile(request):
    #return HttpResponse("You're at the student view of the Game Overview")
    return render(request, 'studentprofile.html')



