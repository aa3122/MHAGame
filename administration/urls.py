from django.urls import path
from . import views
from .views import *
# from django.views.generic import list_detail

urlpatterns = [
path('', adminDashboard.as_view(), name="adminDashboard"),
path('creategame', adminCreateGameView.as_view(), name="adminCreateGame"),
path('viewgames', adminViewGame.as_view(), name="adminViewGame"),
path('viewstudents/<int:pk>', adminViewStudents.as_view(), name="adminViewStudents"),
path('viewgamestats/<int:pk>', adminViewGameStats.as_view(), name="adminViewGameStats"),
path('managegame/<int:pk>', adminManageGameView.as_view(), name = 'adminManageGameView'),
path('gameedit/<int:pk>', adminGameEdit.as_view(), name = 'adminGameEdit'),
path('profile', profile.as_view(), name='profile')

    ]