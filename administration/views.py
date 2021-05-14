from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from login.models import Student 
from django.contrib.auth import get_user_model
from .models import displayusername
from django.contrib.auth.models import User


@staff_member_required(login_url="/student")
def adminDashboard(request):
	displaynames=User.objects.all()
	#return HttpResponse("you're at the administration dashboard :)")
	return render(request, 'adminDashboard.html', {"displayusername":displaynames})
@staff_member_required(login_url="/student")
def adminCreateGame(request):
	return render(request, 'adminCreateGame.html')
@staff_member_required(login_url="/student")
def adminViewGame(request):
	return render(request, 'adminViewGame.html')
@staff_member_required(login_url="/student")
def adminViewStudents(request):
	return render(request, 'adminViewStudents.html')
@staff_member_required(login_url="/student")
def test(request):
	x = Student.objects.all()
	return render(request, 'test.html', {'x':x})

def testcalender(request):
    return render(request, 'testcalender.html')
