from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from game.models import Game, Session
from .forms import SessionCreateForm
from django.views.generic import ListView, DetailView
@login_required()
def studentDashboard(request):
    return render(request, 'studentDashboard.html')
@login_required()
def calender(request):
    return render(request, 'studentCalender.html')
@login_required()
def studentgamecreate(request):
	allgames = Game.objects.all()
	return render(request, 'studentgamecreate.html',  {"gamelist":allgames})
@login_required()
def gameInput(request):
	game_id = request.POST.get("gameid")
	if request.method == 'POST':
		form = SessionCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Your input has been recieved')
		else:
			form = SessionCreateForm()
			context = {
			'form':form,
			}
	return render(request, 'studentGameInput.html')
@login_required()
def studentGameOverview(ListView):
	Session = Session.objects.all()
	return render(request, 'studentGameOverview.html')
@login_required()
def profile(request):
    return render(request, 'studentprofile.html')

def logout(request):
    logout(request)
