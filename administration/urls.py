from django.urls import path

from . import views

urlpatterns = [
    path('', views.adminDashboard, name='administration'),
    path('creategame', views.adminCreateGame, name='adminCreateGame'),
    path('viewgames', views.adminViewGame, name='adminViewGame'),
    path('viewstudents', views.adminViewStudents, name='adminViewStudents')

]