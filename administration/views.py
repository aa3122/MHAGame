from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from game.models import Game, Session
from student.models import Class, CourseSection
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView,UpdateView, DeleteView
from extra_views import CreateWithInlinesView, InlineFormSet
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy

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

class adminManageGameView(AdminStaffRequiredMixin, DetailView):
	model = Session
	models = Session.objects.all()
	template_name = 'adminManageGame.html'
	

	def get_context_data(self, **kwargs):
		context = super(adminManageGameView, self).get_context_data(**kwargs)
		
		context['session'] = Session.objects.all()
		
		return context

class adminDeleteStudents(AdminStaffRequiredMixin, DeleteView):
	model = Session
	models = Session.objects.all()
	template_name = 'adminConfirmDelete.html'
	# success_url = '/administration/adminViewGame'

	def get_context_data(self, **kwargs):
		context = super(adminDeleteStudents, self).get_context_data(**kwargs)
		
		context['session'] = Session.objects.all()
		context['game'] = Game.objects.all()
		context['user'] = User.objects.all()

		return context

	def get_object(self):
		id_ = self.kwargs.get("pk")
		return get_object_or_404(Session, pk=id_)

	def get_success_url(self):
		return ('/administration/viewgames')



class adminCreateGameView(AdminStaffRequiredMixin, CreateView):
	model = Game
	fields = 'game', 'join_tag', 'course','game_name', 'initial_population', 'initial_budget', 'deadline'
	success_url = 'viewgames'
	def form_valid(self, form):
		form.instance.Instructor = self.request.user
		return super(adminCreateGameView, self).form_valid(form)
	template_name = 'adminCreateGame.html'

class adminGameEdit(AdminStaffRequiredMixin, UpdateView):
	model = Game
	fields = 'game', 'join_tag', 'course','game_name', 'initial_population', 'initial_budget', 'deadline'
	success_url = '/administration/viewgames'
	template_name = 'adminCreateGame.html'



class adminDashboard(AdminStaffRequiredMixin, ListView):
	model = Game
	models = Game.objects.all()
	fields = '__all__'
	template_name = 'adminDashboard.html'
	context_object_name = 'viewstudents'


	def get_queryset(self):
		return Game.objects.filter(Instructor_id=self.request.user).order_by('course')



class adminViewGame(AdminStaffRequiredMixin, ListView):
	model = Game
	template_name = 'adminViewGame.html'

	def get_queryset(self):
		return Game.objects.filter(Instructor_id=self.request.user)

	
class profile(DetailView):
	model = User
	def get(self,request):
		return HttpResponse(render(request, 'adminProfile.html'))




