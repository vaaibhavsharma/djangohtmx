from django.urls import path
from singlepage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forms/', views.forms, name='forms'),
]