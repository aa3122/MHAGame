from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from game.models import Game, Session
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView
from game.forms import SessionForm
from django.contrib.auth.models import User


class studentDashboard(View):
	model = Session
	template_name= 'studentDashboard.html'
	def get(self, request):
		return HttpResponse(render(request, 'studentDashboard.html'))

class calender(View):
	template_name = 'studentCalendar.html'
	def get(self, request):
		return HttpResponse(render(request, 'studentCalendar.html'))

class studentgamecreate(ListView):
	model = Game
	template_name = 'studentgamecreate.html'

class gameInput(CreateView):
	model = Session
	fields = '__all__'
	success_url = "mysessions"
	template_name = 'studentGameInput.html'

class gameedit(UpdateView):
	model = Session
	fields = '__all__'
	template_name = 'studentGameInput.html'
	success_url = '/student/mysessions'

class studentGameOverview(ListView):
	model = Session
	template_name = 'studentGameOverview.html'
	context_object_name = 'mysessions'

	def get_queryset(self):
		return Session.objects.filter(student=self.request.user).order_by('sessionid')
	

class profile(UpdateView):
	model = User
	template_name = 'studentprofile.html'
	def get(self, request):
		return HttpResponse(render(request, 'studentprofile.html'))

def logout(request):
    logout(request)
