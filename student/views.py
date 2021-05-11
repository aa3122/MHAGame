from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student




def calender(request):
    #return HttpResponse("You're on the Student view of the Calender page")
    return render(request, 'studentCalender.html')

def gameInput(request):
    #return HttpResponse("You're at the student view of the Game Input")
    return render(request, 'studentGameInput.html')

def studentGameOverview(request):
    #return HttpResponse("You're at the student view of the Game Overview")
    data = Student.objects.all()

    stu = {
        "student_number": data
    }
    return render(request, 'studentGameOverview.html',stu)

def profile(request):
    #return HttpResponse("You're at the student view of the Game Overview")
    return render(request, 'studentprofile.html')



