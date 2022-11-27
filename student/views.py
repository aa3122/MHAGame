from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from game.models import Game, Session
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages


class studentDashboard(ListView):
	model = Session
	template_name= 'studentDashboard.html'
	context_object_name = 'mysessions'

	def get_queryset(self):
		return Session.objects.filter(student=self.request.user).order_by('session')

class calender(View):
	template_name = 'studentCalendar.html'
	def get(self, request):
		return HttpResponse(render(request, 'studentCalendar.html'))

class studentgamecreate(View):
	success_url = "mysessions"
	failure_url = 'studentgamecreate'
	template_name = 'studentgamecreate.html'
	template_name2 = 'studentgamecreate2.html'
	def get(self, request, pk=None):
		return render(request, self.template_name)

	def post(self, request, pk=None):
		game_tag = request.POST.get("game_txt")
        # Add owner to the model before saving
		try:
			game = Game.objects.get(join_tag = game_tag)
			#Error checking goes here
			session = Session.objects.create(game_tag = game)
			session.student = self.request.user
			session.save()
			return redirect(self.success_url)
		except Game.DoesNotExist:
			comment = 'Please enter a valid join code.'
			return render(request, self.template_name2)

class gameInput(UserPassesTestMixin, UpdateView):
	model = Session
	fields = ('immunization_perc','EDUSmoking_perc','EDUDisease_perc','Screening_perc','TestingLab_perc','TestingPharmo_perc','AnnualPCP_perc','HospitalCare_perc','MentalHealth_perc','EmergencyCare_perc','OutPatientSurg_perc','OutPatientRadio_perc','PhysicianPCP_perc','PhysicianSpec_perc','UrgentCare_perc','HomeHealth_perc','Hospice_perc','LTAC_perc','SkilledNursing_perc','NursingHome_perc','AsstLiving_perc','IndLiving_perc','NameBrand_perc','GenDrugs_perc','SpecialtyDrugs_perc','DurableMedEqu_perc','TobTax_perc','Alcohol_perc','FattyFoods_perc','SugFoods_perc')
	success_url = "mysessions"
	template_name = 'studentGameInput.html'

class gameedit(UserPassesTestMixin, UpdateView):
	model = Session
	models = Session.objects.all()
	fields = ('immunization_perc','EDUSmoking_perc','EDUDisease_perc','Screening_perc','TestingLab_perc','TestingPharmo_perc','AnnualPCP_perc','HospitalCare_perc','MentalHealth_perc','EmergencyCare_perc','OutPatientSurg_perc','OutPatientRadio_perc','PhysicianPCP_perc','PhysicianSpec_perc','UrgentCare_perc','HomeHealth_perc','Hospice_perc','LTAC_perc','SkilledNursing_perc','NursingHome_perc','AsstLiving_perc','IndLiving_perc','NameBrand_perc','GenDrugs_perc','SpecialtyDrugs_perc','DurableMedEqu_perc','TobTax_perc','Alcohol_perc','FattyFoods_perc','SugFoods_perc')
	template_name = 'studentGameInput.html'
	success_url = '/student/mysessions'

	def test_func(self):
		Session = self.get_object()
		if self.request.user == Session.student:
			return True
		return False

	def handle_no_permission(self):
		return redirect('/student')

class studentGameOverview(ListView):
	model = Session
	template_name = 'studentGameOverview.html'
	context_object_name = 'sessions'

	def get_queryset(self):
		sessions =  Session.objects.filter(student=self.request.user).order_by('session')
		for session in sessions:
			session.game = Game.objects.filter(join_tag = session)
		return sessions

class profile(UpdateView):
	model = User
	fields = ['first_name', 'last_name']
	template_name = 'studentprofile.html'
	slug_field = 'username'
	slug_url_kwarg = 'slug'
	success_url = '/student'

	def get_object(self):
		return self.request.user
	def get_context_data(self, **kwargs):
		context = super(profile, self).get_context_data(**kwargs)

		context['user'] = User.objects.all()

		return context

def logout(request):
    logout(request)
