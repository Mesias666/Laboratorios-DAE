from django.urls import path
from . import views

urlpatterns = [
    path('sumar/<int:numero1>/<int:numero2>/', views.sumar, name='sumar'),
    path('restar/<int:numero1>/<int:numero2>/', views.restar, name='restar'),
    path('multiplicar/<int:numero1>/<int:numero2>/', views.multiplicar, name='multiplicar'),
]