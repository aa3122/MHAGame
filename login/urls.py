from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('forgotpassword', views.forgotpassword, name="forgotpassword),

]