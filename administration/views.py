from django.shortcuts import render
from django.http import HttpResponse

from login.models import Student 

def adminDashboard(request):
	#return HttpResponse("you're at the administration dashboard :)")
	return render(request, 'adminDashboard.html')

def adminCreateGame(request):
	return render(request, 'adminCreateGame.html')

def adminViewGame(request):
	return render(request, 'adminViewGame.html')

def adminViewStudents(request):
	return render(request, 'adminViewStudents.html')

def test(request):
	x = Student.objects.all()
	return render(request, 'test.html', locals())
