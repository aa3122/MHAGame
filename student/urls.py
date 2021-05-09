from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentDashboard, name="studentDashboard"),
    path('gameOverview', views.studentGameOverview, name="studentGameOverview"),
    path('Calender', views.calender, name="calender")
    path('gameInput', views.gameInput, name='gameInput')
]