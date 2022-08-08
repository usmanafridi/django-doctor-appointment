
from . import views
from django.urls import path

urlpatterns = [
   
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('make-appointment/', views.AppointmentView.as_view(), name='appointment'),
    path('manage-appointment/', views.ManageAppointmentView.as_view(), name='manage-appointment'),
]
