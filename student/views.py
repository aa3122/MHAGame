from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
# from game.models import game
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
@login_required()
def studentDashboard(request):
    return render(request, 'studentDashboard.html')
@login_required()
def calender(request):
    return render(request, 'studentCalender.html')
@login_required()
def gameInput(request):
    return render(request, 'studentGameInput.html')
@login_required()
def studentGameOverview(request):
    query_results = Student.objects.all()
    return render(request, 'studentGameOverview.html', {'query_results':query_results})
@login_required()
def profile(request):
    return render(request, 'studentprofile.html')

def logout(request):
    logout(request)
