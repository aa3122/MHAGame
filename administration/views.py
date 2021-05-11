from django.shortcuts import render
from django.http import HttpResponse

def adminDashboard(request):
	#return HttpResponse("you're at the administration dashboard :)")
	return render(request, 'adminDashboard.html')

def adminCreateGame(request):
	return render(request, 'adminCreateGame.html')

def adminViewGame(request):
	return render(request, 'adminViewGame.html')

def adminViewStudents(request):
	return render(request, 'adminViewStudents.html')
<<<<<<< HEAD

def test(request):
	return render(request, 'test.html')
=======
>>>>>>> 1360cf667157ff4ed5f76ab389bf7044c6fcb126
