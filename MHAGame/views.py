from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from . forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("student:studentDashboard")

def login_redirect(request):
	return redirect("/accounts/login")
def signup_redirect(request):
	return redirect("/accounts/signup")
def reset_redirect(request):
	return redirect("/accounts/login")



def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login')
		else:
			print(form.errors)

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()

	return render(request, 'registration/signup.html', args)