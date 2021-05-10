from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="loginpage"),
    path('forgotpassword', views.forgotpassword, name="forgotpassword")

]