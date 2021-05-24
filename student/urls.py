from django.urls import path
from . import views
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(studentDashboard.as_view(), login_url='/accounts/login'),name="studentDashboard"),
        path('mysessions', login_required(studentGameOverview.as_view(), login_url='/accounts/login'),name="mysessions"),
    path('calender', login_required(calender.as_view(), login_url='/accounts/login'), name="calender"),
    path('gameinput', login_required(gameInput.as_view(), login_url='/accounts/login'), name='gameInput'),
        path('profile', login_required(profile.as_view(), login_url='/accounts/login'), name='profile'),
    path('gamecreate', login_required(studentgamecreate.as_view(), login_url='/accounts/login'), name="studentgamecreate"),
    path('mysessions/<int:pk>', login_required(gameedit.as_view(), login_url='/accounts/login'), name = 'gameedit')
]