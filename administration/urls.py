from django.urls import path

from . import views

urlpatterns = [
    path('', views.adminDashboard, name='administration'),
    path('creategame', views.adminCreateGame, name='adminCreateGame'),
    path('viewgames', views.adminViewGame, name='adminViewGame'),
<<<<<<< HEAD
    path('viewstudents', views.adminViewStudents, name='adminViewStudents'),
    path('test',views.test, name='test')
=======
    path('viewstudents', views.adminViewStudents, name='adminViewStudents')
>>>>>>> 1360cf667157ff4ed5f76ab389bf7044c6fcb126

]