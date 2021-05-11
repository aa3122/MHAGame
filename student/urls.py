from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentDashboard, name="studentDashboard"),
    path('gameOverview', views.studentGameOverview, name="studentGameOverview"),
    path('calender', views.calender, name="calender"),
    path('gameinput', views.gameInput, name='gameInput'),
    path('profile', views.profile, name='profile')
]