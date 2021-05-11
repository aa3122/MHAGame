from django.urls import path

from . import views

urlpatterns = [
    path('', views.adminDashboard, name='administration')

]