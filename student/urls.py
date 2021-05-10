from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentDashboard, name="studentDashboard"),
    path('gameoverview', views.studentGameOverview, name="studentGameOverview"),
    path('calender', views.calender, name="calender"),
    path('gameinput', views.gameInput, name='gameInput')
]