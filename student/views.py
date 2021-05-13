from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
@login_required()
def studentDashboard(request):
    #return HttpResponse("You're at the student dashboard")
    return render(request, 'studentDashboard.html')
@login_required()
def calender(request):
    #return HttpResponse("You're on the Student view of the Calender page")
    return render(request, 'studentCalender.html')
@login_required()
def gameInput(request):
    #return HttpResponse("You're at the student view of the Game Input")
    return render(request, 'studentGameInput.html')
@login_required()
def studentGameOverview(request):
    #return HttpResponse("You're at the student view of the Game Overview")
    query_results = Student.objects.all()
    return render(request, 'studentGameOverview.html', {'query_results':query_results})
#@staff_member_required(login_url="/student")
def profile(request):
    #return HttpResponse("You're at the student view of the Game Overview")
    return render(request, 'studentprofile.html')

def logout(request):
    logout(request)
