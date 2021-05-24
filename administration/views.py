from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from game.models import Game, Session
from student.models import Class,  CourseSection
from django.views.generic import ListView, DetailView, CreateView, View
from extra_views import CreateWithInlinesView, InlineFormSet



class adminDashboard(View):
	model = Game
	template_name = 'adminDashboard.html'
	def get(self,request):
		# displaynames=User.objects.exclude(is_staff = 1)
		return HttpResponse(render(request, 'adminDashboard.html'))

# class adminCreateGameView(CreateView):
	# model = Game
	# fields = '__all__'
	# success_url = 'viewgames'
	# template_name = 'adminCreateGame.html'


class adminPullUser(InlineFormSet):
    model = User   
    # fields = 'username'

class adminCreateGameView(CreateWithInlinesView):
	model = Game
	fields = '__all__'
	inlines = [adminPullUser]
	success_url = 'viewgames'
	template_name = 'adminCreateGame.html'

  


class adminViewGame(ListView):
	model = Game
	template_name = 'adminViewGame.html'

class adminViewStudents(ListView):
	model = User
	template_name = 'adminViewStudents.html'

class profile(DetailView):
	model = User
	def get(self,request):
		return HttpResponse(render(request, 'adminProfile.html'))

# @staff_member_required(login_url="/student")
# def adminDashboard(request):
# 	displaynames=User.objects.exclude(is_staff = 1)
# 	return render(request, 'adminDashboard.html', {"displayusername":displaynames})

# @staff_member_required(login_url="/student")
# def adminCreateGame(request):
# 	return render(request, 'adminCreateGame.html')

# @staff_member_required(login_url="/student")
# def adminViewGame(request):
# 	displaynames=User.objects.all()
# 	displaygames=Game.objects.all()
# 	return render(request, 'adminViewGame.html', {"displaygames":displaygames, "displaynames":displaynames})

# @staff_member_required(login_url="/student")
# def adminViewStudents(request):
# 	displaynames=User.objects.exclude(is_staff = 1)
# 	return render(request, 'adminViewStudents.html', {"displayusername":displaynames})

# @staff_member_required(login_url="/student")
# def adminProfile(request):
# 	return render(request, 'adminProfile.html')

# class adminCreateGameView(CreateView):
# 	model = Game
# 	template_name = 'adminCreateGame.html'
# 	fields = '__all__'

