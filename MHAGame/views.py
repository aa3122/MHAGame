from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("student:studentDashboard")

def login_redirect(request):
	return redirect("/accounts/login")