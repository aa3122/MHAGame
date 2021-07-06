from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from game.models import Game, Session
from student.models import Class, CourseSection
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView,UpdateView
from extra_views import CreateWithInlinesView, InlineFormSet
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.contrib.auth.views import redirect_to_login

from django.shortcuts import get_object_or_404


class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('studentDashboard'))

class adminViewGameStats(AdminStaffRequiredMixin, DetailView):
	template_name = 'adminViewGameStats.html'
	model = Game
	success_url = '/administration/viewGameStats'


	def get_context_data(self, **kwargs):
		context = super(adminViewGameStats, self).get_context_data(**kwargs)
		
		context['session'] = Session.objects.all()
		
		return context        
           

class adminViewStudents(AdminStaffRequiredMixin, DetailView):
	template_name = 'adminViewStudents.html'
	model = Game
	success_url = '/administration/viewstudents'


	def get_context_data(self, **kwargs):
		context = super(adminViewStudents, self).get_context_data(**kwargs)
		
		context['session'] = Session.objects.all()
		
		return context



class adminDashboard(AdminStaffRequiredMixin, ListView):
	model = Game
	models = Game.objects.all()
	fields = '__all__'
	template_name = 'adminDashboard.html'
	context_object_name = 'viewstudents'


	def get_queryset(self):
		return Game.objects.filter(Instructor_id=self.request.user).order_by('course')

class adminCreateGameView(AdminStaffRequiredMixin, CreateView):
	model = Game
	fields = 'game', 'join_tag', 'course','game_name', 'initial_population', 'initial_budget'
	success_url = 'viewgames'
	def form_valid(self, form):
		form.instance.Instructor = self.request.user
		return super(adminCreateGameView, self).form_valid(form)
	template_name = 'adminCreateGame.html'

class adminGameEdit(AdminStaffRequiredMixin, UpdateView):
	model = Game
	fields = 'game', 'join_tag', 'course','game_name', 'initial_population', 'initial_budget'
	success_url = '/administration/viewgames'
	template_name = 'adminCreateGame.html'




class adminViewGame(AdminStaffRequiredMixin, ListView):
	model = Game
	template_name = 'adminViewGame.html'

	def get_queryset(self):
		return Game.objects.filter(Instructor_id=self.request.user)

	
class adminManageGameView(AdminStaffRequiredMixin, DetailView):
	model = Session
	models = Session.objects.all()
	template_name = 'adminManageGame.html'
	

	def get_context_data(self, **kwargs):
		context = super(adminManageGameView, self).get_context_data(**kwargs)
		
		context['session'] = Session.objects.all()
		
		return context
class profile(DetailView):
	model = User
	def get(self,request):
		return HttpResponse(render(request, 'adminProfile.html'))




