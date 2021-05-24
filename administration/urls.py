from django.urls import path
from . import views
from .views import *

urlpatterns = [
path('', adminDashboard.as_view(), name="adminDashboard"),
path('creategame', adminCreateGameView.as_view(), name="adminCreateGame"),
path('viewgames', adminViewGame.as_view(), name="adminViewGame"),
path('viewstudents', adminViewStudents.as_view(), name="adminViewStudents"),
path('profile', profile.as_view(), name='profile')

    ]