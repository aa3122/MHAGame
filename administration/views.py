from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from .models import displayusername
from django.contrib.auth.models import User
from game.models import Game


@staff_member_required(login_url="/student")
def adminDashboard(request):
	displaynames=User.objects.exclude(is_staff = 1)
	return render(request, 'adminDashboard.html', {"displayusername":displaynames})
@staff_member_required(login_url="/student")
def adminCreateGame(request):
	return render(request, 'adminCreateGame.html')
@staff_member_required(login_url="/student")
def adminViewGame(request):
	displaynames=User.objects.all()
	displaygames=Game.objects.all()
	return render(request, 'adminViewGame.html', {"displaygames":displaygames, "displaynames":displaynames})
@staff_member_required(login_url="/student")
def adminViewStudents(request):
	displaynames=User.objects.exclude(is_staff = 1)
	return render(request, 'adminViewStudents.html', {"displayusername":displaynames})
@staff_member_required(login_url="/student")
#def test(request):
#	x = Student.objects.all()
#	return render(request, 'test.html', {'x':x})

def testcalender(request):
    return render(request, 'testcalender.html')

@staff_member_required(login_url="/student")
def adminProfile(request):
	return render(request, 'adminProfile.html')

