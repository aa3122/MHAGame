from django.urls import path

from . import views

urlpatterns = [
    path('', views.administrator, name='administrator')

]