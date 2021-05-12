from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from . forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.template.context_processors import csrf


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("student:studentDashboard")

def login_redirect(request):
	return redirect("/accounts/login")

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	args = {}
	args.update(csrf(request))

	args['form'] = SignUpForm()

	return render(None, 'registration/signup.html', args)